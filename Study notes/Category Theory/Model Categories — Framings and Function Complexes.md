---
type: topic
subject: model-categories
chapter: "Hovey Ch.5"
title: "Model Categories — Framings and Function Complexes"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation Registry

This chapter studies homotopy theory of *diagrams* and the *derived mapping spaces* every homotopy theory secretly carries. The running convention is that $\mathcal{M}$ is an arbitrary [[Def - Model Category|model category]] — we make *no* assumption that it is simplicial, cofibrantly generated, or enriched, because the whole point of framings is that mapping *spaces* exist without such hypotheses. The indexing categories are restricted instead: they must be **Reedy categories**, of which the simplex category $\Delta$ and its opposite $\Delta^{op}$ are the prototypes. We follow Hovey's Chapter 5 (the parallel treatment is Hirschhorn's *Model Categories and Their Localizations*).

- $\mathcal{M}, \mathcal{N}$ — model categories; $\mathcal{W}$ — weak equivalences ($\xrightarrow{\sim}$); $\rightarrowtail$, $\twoheadrightarrow$ — cofibrations, fibrations
- $\varnothing$, $*$ — initial and terminal object; $QX$, $RY$ — cofibrant and fibrant replacement
- $\mathcal{R}$ — a Reedy category; $\mathcal{R}^{+}$ — direct subcategory (raises degree); $\mathcal{R}^{-}$ — inverse subcategory (lowers degree); $\deg$ — degree function
- $\mathcal{M}^{\mathcal{R}}$ — the category of $\mathcal{R}$-diagrams in $\mathcal{M}$; $X_r = X(r)$ — value at $r$
- $L_r X$ — latching object (colimit of $X$ over $\mathcal{R}^{+}$ below $r$); $M_r X$ — matching object (limit of $X$ over $\mathcal{R}^{-}$ above $r$)
- $\ell_r : L_r X \to X_r$ — latching map; $m_r : X_r \to M_r X$ — matching map
- relative latching map $X_r \cup_{L_r X} L_r Y \to Y_r$; relative matching map $X_r \to Y_r \times_{M_r Y} M_r X$
- $\Delta$ — simplex category, objects $[n] = \{0 < \cdots < n\}$; $\Delta^n = \Delta(-,[n])$ — standard $n$-simplex; $\Lambda^n_i$ — horn
- $X^{\bullet} : \Delta \to \mathcal{M}$ — a cosimplicial object, $[n] \mapsto X^n$; $Y_{\bullet} : \Delta^{op} \to \mathcal{M}$ — a simplicial object, $[n] \mapsto Y_n$
- $cX$ — the constant (co)simplicial object at $X$
- $\mathbf{sSet}$ — simplicial sets; $\mathrm{Ho}(\mathbf{sSet})$ — its homotopy category
- $\mathrm{map}(X, Y) \in \mathrm{Ho}(\mathbf{sSet})$ — the homotopy function complex (derived mapping space); $[X,Y] = \mathrm{Ho}(\mathcal{M})(X,Y)$
- $X \otimes K$, $Y^K$ — homotopical tensor and cotensor of an object with a simplicial set $K$

---

# Motivation

Quillen's homotopy category $\mathrm{Ho}(\mathcal{M})$ has a fatal poverty: its hom-sets are *sets*. The morphisms from $X$ to $Y$ are homotopy classes of maps — and a *class* is a $\pi_0$, which has thrown away the homotopies between homotopic maps, the homotopies between those, and every higher layer. In topology this is intolerable: the maps from $X$ to $Y$ form a *space* $\mathrm{Map}(X, Y)$ with rich higher homotopy, and the set $[X, Y]$ is just its set of components. This chapter restores the lost structure for *any* model category. The central object is the **homotopy function complex** $\mathrm{map}(X, Y)$, a simplicial set with
$$\pi_0\,\mathrm{map}(X, Y) \;\cong\; [X, Y],$$
whose higher homotopy groups are the higher homotopies. It is the **derived hom** of the homotopy theory — the homotopical refinement of $\mathrm{Hom}$, exactly as $\mathbf{R}\mathrm{Hom}$ refines $\mathrm{Hom}$ of modules.

The obstacle is that there is no obvious way to *build* this space from the bare axioms of a model category. In a **simplicial model category** — one enriched, tensored, and cotensored over $\mathbf{sSet}$ — the mapping space is given, and life is easy. But most model categories are not simplicial. Hovey's solution is **framings**: a device that manufactures, in any model category, a homotopically-correct version of the missing structure. A **cosimplicial frame** on $X$ is a homotopically meaningful "$X \otimes \Delta^{\bullet}$" — a cosimplicial object interpolating $X$ with all its iterated cylinders, organized so that level $1$ is a cylinder, level $2$ a homotopy between homotopies, and so on. Applying the corepresentable $\mathcal{M}(-, Y)$ to it produces the function complex.

To make frames precise we need homotopy theory of *diagrams*, and that is the chapter's first half. The key structural backbone is the chain of model structures on a diagram category $\mathcal{M}^{\mathcal{R}}$:
$$\text{projective} \;\preceq\; \text{Reedy} \;\preceq\; \text{injective},$$
ordered by their cofibrations. The projective and injective structures exist only for nice $\mathcal{M}$; the **Reedy structure** in the middle exists for *every* $\mathcal{M}$, at the price of requiring the shape $\mathcal{R}$ to be a Reedy category. It is built by the **latching/matching** machinery: a diagram is assembled one degree at a time, with the latching object $L_r X$ holding "what the lower degrees already force" and the matching object $M_r X$ holding "the boundary the new data must respect." This is the homotopy-theoretic analogue of building a CW complex cell by cell.

The chapter then closes the loop. A frame is a Reedy (co)fibrant replacement of a constant diagram; the function complex is the corepresentable applied to a frame; and the decisive theorem is that the answer is **independent of the frame** and agrees whether computed cosimplicially (source side) or simplicially (target side). The upshot is a slogan that will recur through higher algebra: *every model category presents an $\infty$-category, whose mapping spaces are the homotopy function complexes.* A reader entering this chapter should have refreshed [[Def - Model Category|model categories]] and their axioms, [[Def - Cofibrant and Fibrant Objects|(co)fibrant replacement]], the [[Def - Cylinder Object, Path Object, and Homotopy|cylinder/path object]] formulation of homotopy, [[Def - Limit and Colimit|limits and colimits]] (the latching/matching objects are these), and [[Def - Simplicial Set|simplicial sets]] with the simplex category $\Delta$.

---

# Concept Map

## §1 Reedy Categories and Diagram Model Structures

- **[[Def - Reedy Category and the Reedy Model Structure]]**
	- A Reedy category $\mathcal{R}$ has a degree function $\deg$ and two wide subcategories $\mathcal{R}^{+}$ (raising degree) and $\mathcal{R}^{-}$ (lowering degree) such that every morphism factors *uniquely* as an inverse map followed by a direct map. This makes $\mathcal{M}^{\mathcal{R}}$ into a model category via latching objects $L_r X = \operatorname{colim}_{\mathcal{R}^{+}\downarrow r} X$ and matching objects $M_r X = \lim_{r\downarrow\mathcal{R}^{-}} X$: Reedy cofibrations have relative latching maps that are cofibrations, Reedy fibrations have relative matching maps that are fibrations, and weak equivalences are objectwise. The simplex category $\Delta$ (cofaces direct, codegeneracies inverse) is the prototype, so cosimplicial and simplicial objects carry Reedy structures.

- **[[Thm - Diagrams over a Reedy Category Form a Model Category]]**
	- For any Reedy category $\mathcal{R}$ and any model category $\mathcal{M}$, the three classes above make $\mathcal{M}^{\mathcal{R}}$ a model category — *with no extra hypothesis on $\mathcal{M}$*. The proof is an induction on degree: extending a diagram by one degree is exactly factoring the canonical map $L_r X \to M_r X$ through $X_r$, and a model structure is a machine for factoring maps. The Reedy structure inherits cofibrant generation, properness, simpliciality, and monoidal structure from $\mathcal{M}$, and sits between the projective and injective structures. Specializing to $\Delta, \Delta^{op}$ gives the model categories of cosimplicial and simplicial objects, hence frames.

> [!tip] Unlocked: Homotopy Limits, Colimits, and the Bousfield–Kan Spectral Sequence *(from Stable Homotopy Theory)*
> For a Reedy shape, $\operatorname{holim}$ and $\operatorname{hocolim}$ are the strict limit/colimit of a Reedy fibrant/cofibrant replacement; the degree filtration is the **Tot-tower**, and its spectral sequence is the **Bousfield–Kan spectral sequence** behind the Adams and descent spectral sequences. Reedy categories are the standard machine for **homotopy limits and colimits** over $\Delta^{op}$, $\Delta$, towers, and cubes.

> [!tip] Unlocked: Complete Segal Spaces and Diagram ∞-Categories *(from Higher Category Theory)*
> Reedy fibrant simplicial spaces are the home of Rezk's **complete Segal space** model of $(\infty,1)$-categories, and Reedy model structures present diagram **∞-categories** $\mathrm{Fun}(N\mathcal{R}, \mathcal{C})$. Allowing automorphisms gives **generalized Reedy categories**, indexing symmetric and equivariant homotopy theory.

- **[[Ex - The simplex category is a Reedy category]]** (⭐)
	- Verify $\Delta$ is Reedy with cofaces direct, codegeneracies inverse, and $\deg[n]=n$, deducing the epi-mono factorization is unique.

- **[[Ex - Latching and matching objects for cosimplicial and simplicial objects]]** (⭐⭐)
	- Compute $L_n$ and $M_n$ explicitly for $\Delta$ and $\Delta^{op}$, identifying latching as "degenerate part" and matching as "compatible boundaries."

- **[[Ex - Towers and cubes as Reedy diagram model structures]]** (⭐⭐)
	- Show the tower poset $\omega$ and the cube poset are Reedy, and read off when ordinary (co)limit computes the homotopy (co)limit.

> [!note] Exercise Index — §1 Reedy Categories and Diagram Model Structures
> [[Exercise Index - §1 Reedy Categories and Diagram Model Structures]]

## §2 Framings

- **[[Def - Cosimplicial and Simplicial Frame]]**
	- A cosimplicial frame on $X$ is a Reedy-cofibrant cosimplicial object $X^{\bullet}$ with $X^0 \simeq X$ and all structure maps weak equivalences — a homotopically-correct "$X \otimes \Delta^{\bullet}$," with level $1$ a [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]] and higher levels recording iterated homotopies. Dually a simplicial frame on $Y$ is a Reedy-fibrant simplicial object with level $1$ a path object. A framing on $\mathcal{M}$ is a functorial choice of both; it makes $\mathcal{M}$ tensored and cotensored over $\mathbf{sSet}$ *up to homotopy* via coend/end formulas $X\otimes K = \int^{[n]} K_n \cdot X^n$, $\;Y^K = \int_{[n]} (Y_n)^{K_n}$.

> [!tip] Unlocked: Every Model Category is a Homotopical sSet-Module *(from Model Categories)*
> Framings upgrade *any* model category to one tensored/cotensored over $\mathbf{sSet}$ up to homotopy — so mapping *spaces* (not just mapping *sets*) exist in every homotopy theory, even those with no strict simplicial enrichment. This is the structural payoff that frees homotopy theory from the requirement of being a simplicial model category.

> [!tip] Unlocked: Cosimplicial Resolutions and Derived Functors *(from Homological Algebra)*
> A frame is a **simplicial/cosimplicial resolution** run homotopically; under Dold–Kan it corresponds to a projective resolution, so frames are the homotopical generalization of "resolve to compute derived functors." This is the bridge to **derived functors** and **derived categories**.

- **[[Ex - The constant cosimplicial object is rarely a frame]]** (⭐⭐)
	- Show the constant object $cX$ fails Reedy cofibrancy because its degree-$1$ latching map is the fold map $X \sqcup X \to X$, which is generically not a cofibration.

- **[[Ex - In a simplicial model category the tensor with simplices is a frame]]** (⭐⭐)
	- Verify $X \otimes \Delta^{\bullet}$ is a cosimplicial frame on a cofibrant $X$, so framings recover the strict structure when present.

- **[[Ex - Level one of a frame is a cylinder object]]** (⭐)
	- Extract from any cosimplicial frame a cylinder object on $X$, recovering [[Def - Cylinder Object, Path Object, and Homotopy|left homotopy]].

> [!note] Exercise Index — §2 Framings
> [[Exercise Index - §2 Framings]]

## §3 Homotopy Function Complexes

- **[[Def - Homotopy Function Complex]]**
	- The homotopy function complex $\mathrm{map}(X, Y)$ is the simplicial set $[n] \mapsto \mathcal{M}(X^n, Y)$ for a cosimplicial frame $X^{\bullet}$ and fibrant $Y$ (or dually $\mathcal{M}(X, Y_n)$). It is the derived mapping space: a Kan complex with $\pi_0\,\mathrm{map}(X,Y) = [X,Y]$ and higher $\pi_n$ recording higher homotopies. It is the model-categorical computation of the **mapping space** of the underlying $\infty$-category $\mathcal{M}[\mathcal{W}^{-1}]$, and in $\mathbf{Ch}(R)$ it packages $\mathbf{R}\mathrm{Hom}$, with $\pi_n = \mathrm{Ext}^{-n}$.

- **[[Thm - Framings Compute Homotopy Function Complexes]]**
	- For cofibrant $X$ and fibrant $Y$: $\mathrm{map}(X,Y)$ is a Kan complex; it is independent of the chosen frame up to weak equivalence; the cosimplicial (source) and simplicial (target) computations agree via the bisimplicial diagonal; and $\pi_0 = [X,Y]$. So every model category has a well-defined derived mapping space, refining the hom-set of $\mathrm{Ho}(\mathcal{M})$ into a space and agreeing with the simplicial mapping object when $\mathcal{M}$ is a simplicial model category. The proof reduces every claim to Reedy (co)fibrancy of frames plus the fibrant-target lifting that makes the complex Kan.

> [!tip] Unlocked: Model Categories Present ∞-Categories *(from Higher Category Theory)*
> The homotopy function complex is the **mapping space** $\mathrm{Map}_{\mathcal{M}[\mathcal{W}^{-1}]}(X, Y)$ of the **∞-category** underlying $\mathcal{M}$; this theorem is the proof that a model category presents an ∞-category, the foundational fact of **higher algebra** (Lurie). It agrees with the **Dwyer–Kan simplicial localization**, which computes the same mapping space by resolving morphisms instead of objects.

> [!tip] Unlocked: Derived Hom, Ext, and the Derived Category *(from Homological Algebra)*
> For chain complexes the homotopy function complex is the space-level **$\mathbf{R}\mathrm{Hom}$**, with $\pi_*$ the **Ext** groups, and its homotopy category is the **derived category**. The theorem is the homotopical proof that derived hom is resolution-independent — the higher-categorical face of "$\mathrm{Ext}$ does not depend on the resolution."

- **[[Ex - Pi-zero of the function complex is the homotopy classes]]** (⭐)
	- Show $\pi_0\,\mathrm{map}(X,Y) = [X,Y]$ by identifying $0$-simplices with maps and $1$-simplices with homotopies.

- **[[Ex - The function complex of simplicial sets is the internal hom]]** (⭐⭐)
	- For Kan complexes $X, Y$ identify $\mathrm{map}(X,Y) \simeq Y^X$ using the frame $X \times \Delta^{\bullet}$.

- **[[Ex - Homotopy function complexes in chain complexes compute Ext]]** (⭐⭐⭐)
	- Using a projective resolution as a frame, prove $\pi_n\,\mathrm{map}(M,N) \cong \mathrm{Ext}^{-n}_R(M,N)$ in $\mathbf{Ch}(R)$.

> [!note] Exercise Index — §3 Homotopy Function Complexes
> [[Exercise Index - §3 Homotopy Function Complexes]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The proof-targets in this chapter cluster into five recurring shapes. The first is **"this diagram category is a model category"**: showing $\mathcal{M}^{\mathcal{R}}$ carries the Reedy structure, which reduces to verifying the indexing $\mathcal{R}$ is Reedy and then quoting [[Thm - Diagrams over a Reedy Category Form a Model Category]]. The second is **"this object is Reedy (co)fibrant"**: checking that each latching map is a cofibration (or each matching map a fibration), the verification that certifies a candidate frame. The third is **"this is a frame"**: Reedy cofibrancy *plus* all structure maps being weak equivalences — the two conditions one must always check together. The fourth is **"this simplicial set is the homotopy function complex"**: showing a candidate computation (a strict mapping object, a $\mathbf{R}\mathrm{Hom}$, a topological mapping space) agrees with $\mathrm{map}(X,Y)$, which by frame-independence amounts to exhibiting it as a corepresentable applied to *some* frame. The fifth is **"these two computations / model categories give the same mapping space"**: invoking frame-independence or a Quillen equivalence to transport derived mapping spaces. Recognizing which of the five you are chasing tells you immediately whether to reach for the latching machinery, the frame conditions, or the comparison theorem.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **A Reedy structure on the shape** is the richest source: once $\mathcal{R}$ is Reedy, the entire diagram homotopy theory unlocks, including frames and homotopy (co)limits. **Cofibrancy of the source and fibrancy of the target** is the pairing that recurs everywhere — it is what makes left and right homotopy agree, what makes the function complex a Kan complex, and what makes derived functors well-defined; whenever a homotopy invariant is wanted, the first move is to (co)fibrantly replace. **A chosen resolution** — projective resolution, CW approximation, cofibrant simplicial resolution — is a disguised frame, so "I already resolved $X$" means "I have the frame." **A strict simplicial enrichment**, when present, supplies the canonical frame $X \otimes \Delta^{\bullet}$ and collapses the abstract theory to the concrete mapping object. **A Quillen equivalence** transports all derived mapping spaces, because it preserves frames up to weak equivalence. The recurring move is to route a source to a target: a Reedy shape routes through the diagram-model-structure theorem to frames; a (co)fibrant–fibrant pair routes through the framing theorem to a Kan complex; a resolution routes to a concrete computation of $\mathrm{map}$. The [[Model Categories — Framings and Function Complexes#Problem-Solving Strategy|Problem-Solving Strategy]] makes these routes explicit.

---

# Legal Operations

These are the moves nearly every problem in this chapter is assembled from. When stuck, scan the list and try each. Everything is self-contained.

**Legal operations:**

1. **Find the degree function and the direct/inverse split.** To recognize a category $\mathcal{R}$ as Reedy, assign each object an ordinal degree and sort the non-identity morphisms into degree-raising (direct) and degree-lowering (inverse), then check unique factorization. *Trigger:* you are handed a diagram shape and want to do homotopy theory on diagrams of that shape. *Pattern:* "the maps that raise dimension are $\mathcal{R}^{+}$, those that lower it are $\mathcal{R}^{-}$, and epi-mono factorization is the unique factorization." This is the entry point to [[Thm - Diagrams over a Reedy Category Form a Model Category]].

2. **Compute a latching or matching object as a colimit or limit.** The latching object $L_r X$ is the colimit of $X$ over the direct maps into $r$ from strictly lower degree; the matching object $M_r X$ is the limit over the inverse maps out of $r$. *Trigger:* you must check Reedy (co)fibrancy or build a frame. *Pattern:* "list the lower-degree objects mapping in (out), take their colimit (limit) in $\mathcal{M}$." For [[Def - Simplicial Set|simplicial sets]] the latching object is the degenerate simplices; for simplicial objects the matching object is the compatible boundary.

3. **Check Reedy cofibrancy by checking each latching map is a cofibration.** An object $X$ is Reedy cofibrant exactly when every absolute latching map $L_r X \to X_r$ is a cofibration in $\mathcal{M}$. *Trigger:* you want to certify a candidate frame or a cofibrant diagram. *Pattern:* "Reedy cofibrant ⟺ each latching map is a cofibration"; dually for fibrant via matching maps.

4. **Build a frame as a Reedy-cofibrant replacement of the constant diagram.** To frame $X$, take a Reedy-cofibrant replacement of the constant cosimplicial object $cX$ in $\mathcal{M}^{\Delta}$. *Trigger:* you need a homotopy mapping space, a derived tensor, or a cosimplicial resolution. *Pattern:* "frame = cofibrant replacement of $cX$"; this exists by MC5 in the Reedy structure.

5. **(Co)fibrantly replace before taking any homotopy invariant.** Replace $X$ by a cofibrant $QX$ and $Y$ by a fibrant $RY$ before forming $\mathrm{map}$, a homotopy (co)limit, or a derived functor. *Trigger:* a homotopy invariant is wanted and the objects are not bifibrant. *Pattern:* "resolve, then compute"; the unresolved hom is not homotopy-invariant.

6. **Compute the function complex as a corepresentable of a frame.** Form $\mathrm{map}(X,Y)_n = \mathcal{M}(X^n, RY)$ from a cosimplicial frame, or $\mathcal{M}(QX, Y_n)$ from a simplicial frame. *Trigger:* you want the derived mapping space. *Pattern:* "$n$-simplices = maps out of the degree-$n$ frame piece"; level $1$ is a homotopy, hence $\pi_0 = [X,Y]$.

7. **Pass between the cosimplicial and simplicial computations via the bisimplicial diagonal.** When one side is awkward, compute the other; they agree through $\mathrm{diag}\,\mathcal{M}(X^{\bullet}, Y_{\bullet})$. *Trigger:* the source frame is hard but the target frame is easy, or vice versa. *Pattern:* "row-equivalence + realization lemma ⟹ diagonal computes both," from [[Thm - Framings Compute Homotopy Function Complexes]].

8. **Dualize via $\mathcal{R} \leftrightarrow \mathcal{R}^{op}$ and $\mathcal{M} \leftrightarrow \mathcal{M}^{op}$.** Every statement about Reedy cofibrations / cosimplicial frames / left homotopy has a free dual about Reedy fibrations / simplicial frames / right homotopy. *Trigger:* you have proved the cofibration side and want the fibration side. *Pattern:* "swap $+$ and $-$, swap cofibration and fibration, swap latching and matching"; prove once, get both.

9. **Reduce a horn-filling problem to a lifting problem in $\mathcal{M}$.** A horn $\Lambda^n_i \to \mathcal{M}(X^{\bullet}, Y)$ transposes to extending a map off the horn-part of $X^n$ against $Y \to *$. *Trigger:* you must show a function complex is a Kan complex. *Pattern:* "horn-filling = lift the trivial cofibration (Reedy cofibrancy) against the fibration ($Y$ fibrant)."

10. **Transport mapping spaces along a Quillen equivalence.** A [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] $F \dashv U$ gives $\mathrm{map}_{\mathcal{N}}(FX, Y) \simeq \mathrm{map}_{\mathcal{M}}(X, UY)$. *Trigger:* you want to identify mapping spaces in two equivalent homotopy theories. *Pattern:* "$F$ carries a frame on $X$ to a frame on $FX$, so the corepresentables agree."

**Illegal but tempting operations:**

> [!warning] 1. Putting the Reedy structure on diagrams over a category with non-trivial automorphisms
> It is tempting to apply the Reedy machinery to *any* indexing category. But a category with a non-identity automorphism — a finite group $G$ as a one-object category, for instance — is **not** a Reedy category: the single object has one degree, and a non-identity automorphism neither raises nor lowers it, so it cannot lie in $\mathcal{R}^{+}$ or $\mathcal{R}^{-}$ and there is no unique factorization. The latching/matching induction has nothing to recurse on. The repair is the **generalized Reedy category** of Berger–Moerdijk, which permits automorphisms in each degree and uses isomorphism-equivariant latching objects; only then can equivariant diagrams be handled.

> [!warning] 2. Declaring weak equivalences via latching maps
> Symmetry suggests defining Reedy weak equivalences as the maps whose relative latching maps are weak equivalences, paralleling the cofibrations and fibrations. This is **wrong**. Concretely, take a Reedy weak equivalence between cosimplicial objects whose degree-$0$ terms are weakly equivalent but whose degree-$1$ relative latching maps are not (easy to arrange when the objects are not cofibrant): it is an objectwise weak equivalence, hence a genuine Reedy weak equivalence, but its relative latching maps fail to be weak equivalences. Reedy weak equivalences are **objectwise**, full stop; the latching/matching maps govern *only* cofibrations and fibrations.

> [!warning] 3. Using the constant cosimplicial object $cX$ as a frame
> The constant object $cX$ (all $X^n = X$, all structure maps identities) satisfies the homotopically-constant condition trivially, so it looks like a frame. But it **fails Reedy cofibrancy**: its degree-$1$ latching map is the fold map $X \sqcup X \to X$, which is a cofibration only if $X$ already has a strict cylinder of itself — generically false. Using $cX$ as a frame computes $\mathcal{M}(X, Y)$, the *unresolved* hom-set, which is not homotopy-invariant. The repair is to take a genuine Reedy-cofibrant replacement of $cX$ — that is, to actually resolve.

> [!warning] 4. Computing $\mathrm{map}(X, Y)$ without fibrant $Y$ (or cofibrant $X$)
> It is tempting to form $\mathcal{M}(X^{\bullet}, Y)$ for any $Y$. But without fibrancy of $Y$ the simplicial set is **not a Kan complex** and **not frame-independent** — its homotopy type depends on the chosen frame, so it is not an invariant. The witness is the same phenomenon as computing $\mathbf{R}\mathrm{Hom}(M, N)$ with an arbitrary (non-injective, non-fibrant) $N$: the answer is wrong. The repair is the bifibrant pairing: cofibrantly replace $X$, fibrantly replace $Y$, *then* frame and compute.

---

# Problem-Solving Strategy

The problems in this chapter are won at the moment you classify them, so begin there. Almost every exercise is one of five types, each with a characteristic source and route.

If the problem **asks you to put a model structure on a diagram category** — "show $\mathcal{M}^{\mathcal{R}}$ is a model category" or "show this category of towers/cubes/(co)simplicial objects carries a homotopy theory" — then the route is fixed: recognize $\mathcal{R}$ as a Reedy category by exhibiting the degree function and the direct/inverse split (Legal Operation 1), verify unique factorization, and quote [[Thm - Diagrams over a Reedy Category Form a Model Category]]. The entire difficulty is concentrated in finding the Reedy data; once $\mathcal{R}$ is Reedy, the model structure is automatic and requires nothing of $\mathcal{M}$. The guidance is to look at *which morphisms raise a natural notion of size* — dimension, number of $1$s in a cube, position in a tower — and call those direct.

If the problem **asks you to certify a frame**, the assumption pattern is that you have a candidate (co)simplicial object and must check two things, and the discipline is to check *both* because beginners check only one. First, Reedy cofibrancy: each latching map $L_n X^{\bullet} \to X^n$ is a cofibration (Legal Operation 3), which you verify by computing the latching object as a colimit (Legal Operation 2) and recognizing the latching map as an inclusion of "already-forced" data. Second, homotopical constancy: every coface and codegeneracy is a weak equivalence, so the object really resolves a single $X$ rather than being a genuine diagram. The canonical trap is the constant object $cX$, which passes the second test and fails the first — so always compute the degree-$1$ latching map and confirm it is not the fold map.

If the problem **asks you to compute or identify a homotopy function complex**, the assumption pattern is a (co)fibrant–fibrant pair plus a frame, and the route runs through the corepresentable construction (Legal Operation 6) and [[Thm - Framings Compute Homotopy Function Complexes]]. You do not analyze $\mathrm{map}(X,Y)$ directly; instead you choose the *most convenient* frame — a projective resolution in $\mathbf{Ch}(R)$, the genuine $X \times \Delta^{\bullet}$ in $\mathbf{sSet}$, a CW approximation in $\mathbf{Top}$ — and read off $\mathrm{map}(X,Y)_n = \mathcal{M}(X^n, Y)$. Frame-independence is the licence to pick the easy frame. When one side is awkward, switch to the other via the bisimplicial diagonal (Legal Operation 7); the cosimplicial and simplicial computations always agree.

If the problem **asks you to show a candidate space is the right mapping space** — that a strict simplicial mapping object, a topological mapping space, or $\mathbf{R}\mathrm{Hom}$ equals $\mathrm{map}(X,Y)$ — then the strategy is to exhibit the candidate as a corepresentable applied to *some* frame and invoke frame-independence. In a simplicial model category, $X \otimes \Delta^{\bullet}$ is a frame and the strict mapping object *is* the function complex; in $\mathbf{Ch}(R)$ a projective resolution is a frame and $\mathbf{R}\mathrm{Hom}$ is the function complex. The recognition that "my favorite resolution is a frame" is the whole move.

If the problem **asks you to compare two homotopy theories or two computations**, the route is either frame-independence (two frames, same answer) or a Quillen equivalence (Legal Operation 10), which carries frames to frames and hence identifies all derived mapping spaces. This is how one proves that topological and simplicial mapping spaces agree, or that Quillen-equivalent presentations have the same $\infty$-category.

Finally, a meta-strategy threads through all of the above: **to do homotopy theory, resolve, then compute on the resolution.** Every difficulty in the chapter is an instance of "the strict object is not homotopy-invariant, so replace it by a (co)fibrant one first." A frame is the universal such replacement for the purpose of mapping spaces; Reedy cofibrancy is what makes the replacement correct; and the framing theorem is the guarantee that the answer does not depend on the replacement chosen. Every question in this chapter is, at bottom, the question *"what is the homotopically meaningful version of this construction, and which resolution computes it?"*

---

# Most Reusable Properties

- **[[Thm - Diagrams over a Reedy Category Form a Model Category|The Reedy diagram theorem]]**: $\mathcal{M}^{\mathcal{R}}$ is a model category for any model category $\mathcal{M}$ and any Reedy $\mathcal{R}$. This is the most-used fact because it is *unconditional in $\mathcal{M}$*: it costs nothing about $\mathcal{M}$ and applies the instant a Reedy shape appears. Reach for it whenever you need homotopy theory of diagrams — frames, homotopy (co)limits, totalizations, cubes. **Typical use:** establishing the ambient model structure in which a frame is a (co)fibrant replacement, or in which a homotopy (co)limit is a strict (co)limit after replacement.

- **[[Def - Cosimplicial and Simplicial Frame|Framing]]**: every object has a cosimplicial frame and a simplicial frame, making $\mathcal{M}$ tensored/cotensored over $\mathbf{sSet}$ up to homotopy. The reusable move is "resolve $X$ by a frame to get its iterated cylinders coherently." **Typical use:** building a homotopy mapping space, a derived tensor $X \otimes K$, or a cosimplicial resolution; the level-$1$ piece is always a cylinder object, recovering the homotopy relation of [[Def - Cylinder Object, Path Object, and Homotopy]].

- **[[Def - Homotopy Function Complex|The homotopy function complex]]**: $\mathrm{map}(X,Y)$ is a Kan complex with $\pi_0 = [X,Y]$ and $\pi_n$ the higher homotopies. This is the workhorse for *upgrading hom-sets to hom-spaces*. **Typical use:** any time you need not just the homotopy classes but the space of maps — obstruction theory (via the Kan fibration $\mathrm{map}(X, Y) \to \mathrm{map}(X, Z)$), $\mathrm{Ext}$ computations ($\pi_n = \mathrm{Ext}^{-n}$), or the mapping space of the underlying $\infty$-category.

- **[[Thm - Framings Compute Homotopy Function Complexes|Frame independence]]**: the function complex does not depend on the chosen frame, and cosimplicial = simplicial computations. Its reusability is as a *licence*: it lets you pick the most convenient resolution and trust the answer. **Typical use:** computing $\mathrm{map}$ via a projective resolution, a CW approximation, or a strict enrichment, knowing all three agree; and transporting mapping spaces along a Quillen equivalence.

- **The latching/matching decomposition**: extending a diagram by one degree is factoring $L_r X \to M_r X$ through $X_r$. This is more reusable than any single theorem because it is the *mechanism* behind all of the above — Reedy cofibrancy, frames, homotopy (co)limits, and the Bousfield–Kan spectral sequence all read off the latching/matching data. **Typical use:** any inductive construction or computation indexed by a Reedy category, where you build up degree by degree and the new data lives in the relative latching/matching map.

---

# Bridges

1. **Homological algebra — frames are resolutions and the function complex is $\mathbf{R}\mathrm{Hom}$.** In $\mathbf{Ch}(R)$, a [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] on a complex corresponds, under the Dold–Kan correspondence between simplicial $R$-modules and connective chain complexes, to a projective resolution: the simplicial direction of the frame becomes the homological direction of the resolution. Applying the corepresentable to the frame and taking homotopy groups recovers the classical derived functor — the [[Def - Homotopy Function Complex|homotopy function complex]] $\mathrm{map}(M, N)$ has $\pi_n = \mathrm{Ext}^{-n}_R(M, N)$, so it is the space-level packaging of $\mathbf{R}\mathrm{Hom}(M, N)$. The model-categorical statement that the function complex is resolution-independent is exactly the homological fact that $\mathrm{Ext}$ does not depend on the chosen projective resolution; framings generalize "resolve to compute derived functors" from abelian categories to all model categories. This is the running connection to **derived categories** and **derived functors**.

2. **Higher category theory — the function complex is the $\infty$-categorical mapping space.** A model category $\mathcal{M}$ presents an $(\infty,1)$-**category** $\mathcal{M}[\mathcal{W}^{-1}]$, obtained by inverting the weak equivalences in the $\infty$-categorical sense. Its objects are those of $\mathcal{M}$, and — this is the content of [[Thm - Framings Compute Homotopy Function Complexes]] — its mapping spaces are precisely the homotopy function complexes: $\mathrm{Map}_{\mathcal{M}[\mathcal{W}^{-1}]}(X, Y) \simeq \mathrm{map}(X, Y)$. Reedy fibrant simplicial spaces, built with the Reedy structure of this chapter, are Rezk's **complete Segal space** model of $(\infty,1)$-categories; so the same latching/matching machinery that computes mapping spaces also *presents* the higher categories those mapping spaces live in. Framings are the point-set bridge from Quillen's $1$-categorical homotopy theory to Lurie's $\infty$-categorical higher algebra.

3. **Algebraic topology — recovering mapping spaces and obstruction theory.** For $\mathcal{M} = \mathbf{Top}$ (or [[Def - Simplicial Set|sSet]]) with $X$ a CW complex, the frame is the genuine $X \times |\Delta^{\bullet}|$ and the homotopy function complex is weakly equivalent to the classical mapping space $\mathrm{Map}(X, Y)$ with the compact-open topology; its $\pi_0 = [X, Y]$ is free homotopy classes and its $\pi_n$ the higher homotopies. A fibration $Y \twoheadrightarrow Z$ induces a Kan fibration $\mathrm{map}(X, Y) \to \mathrm{map}(X, Z)$ whose long exact homotopy sequence is the engine of **obstruction theory**: the obstruction to lifting a map $X \to Z$ to $X \to Y$ is the failure of $\pi_0$-surjectivity, controlled by the homotopy groups of the fibre. So this chapter's abstract function complex specializes to the concrete spaces of maps that obstruction theory and the **Federer spectral sequence** study, and the [[Def - Higher Homotopy Group|higher homotopy groups]] of mapping spaces are its invariants.

4. **Stable homotopy theory — totalization and the Bousfield–Kan spectral sequence.** The homotopy limit of a cosimplicial object $X^{\bullet}$ — its **totalization** $\mathrm{Tot}\,X^{\bullet} = \operatorname{holim}_{\Delta} X^{\bullet}$ — is computed by Reedy-fibrantly replacing $X^{\bullet}$ in $\mathcal{M}^{\Delta}$ (via [[Thm - Diagrams over a Reedy Category Form a Model Category]]) and taking the strict limit. The Reedy degree filtration is the **Tot-tower** $\cdots \to \mathrm{Tot}_n \to \mathrm{Tot}_{n-1} \to \cdots$, whose associated spectral sequence is the **Bousfield–Kan spectral sequence** — the framework behind the **Adams spectral sequence** (where $X^{\bullet}$ is the cobar resolution) and descent/completion spectral sequences. The $E_1$ and $E_2$ terms are read directly off the latching/matching data of the cosimplicial object, so the homotopy theory of Reedy diagrams *is* the homotopy theory of these spectral sequences; convergence is exactly a Reedy-fibrancy condition. This connects to the **stable homotopy category** and **triangulated category** machinery of the later chapters.

---

# Insights

**The unifying frame: do homotopy theory by resolving, then computing on the resolution.** Every construction in this chapter is an instance of one idea. The strict, point-set object — the hom-set $\mathcal{M}(X,Y)$, the strict limit $\lim X^{\bullet}$, the underived tensor — is not homotopy-invariant, so you replace the input by a (co)fibrant object and compute there. A **frame** is the universal such replacement for mapping spaces: it is "all iterated cylinders of $X$, made cofibrant and coherent," and applying the corepresentable to it yields the derived mapping space. **Reedy cofibrancy** is precisely the condition that makes the replacement correct, and **frame-independence** is the guarantee that the answer is intrinsic. Once this frame is installed, you see that the homotopy function complex is to the hom-set as $\mathbf{R}\mathrm{Hom}$ is to $\mathrm{Hom}$, as homotopy colimit is to colimit, as derived functor is to functor — all the same move, "resolve then compute," carried out in the simplicial direction so the output is a space rather than a set.

**The true name of a Reedy category is "a CW structure on the indexing shape."** The official definition — degree function, direct and inverse subcategories, unique factorization — is the right thing to *check* but the wrong thing to *think*. The operational picture is that $\mathcal{R}$ is a shape whose objects have a well-ordered dimension, whose direct maps are the "is a face of" inclusions, and whose inverse maps are degeneracies; building a Reedy-cofibrant diagram is building a CW complex of $\mathcal{M}$-objects, attaching the degree-$r$ cell along its boundary $L_r X$. With this picture, the latching object is "the boundary already built," the relative latching map is "the newly attached cell," and the Reedy induction is "build skeleton by skeleton." Every time you see a latching object, picture a boundary; every time you see a relative latching cofibration, picture attaching a cell.

**The simplicial direction is the direction of higher homotopies — that is why $\Delta$ appears.** A single cylinder object computes only $\pi_0$ of the mapping space, the homotopy classes. To recover the whole homotopy type — homotopies between homotopies, and so on — you need a coherent system of *all* iterated cylinders, and the category that organizes iterated homotopies is exactly the simplex category $\Delta$: an $n$-simplex of $\mathrm{map}(X,Y)$ is an $n$-fold homotopy, encoded as a map out of the degree-$n$ frame piece. This is the deep reason frames are *cosimplicial* and function complexes are *simplicial sets*. The hom-set lives in dimension $0$; $\Delta$ supplies all the higher dimensions, and the simplicial identities are what make the higher homotopies compose coherently. Recognizing "$\Delta$ = the shape of coherent higher homotopy" demystifies why simplicial objects pervade homotopy theory.

**Frame-independence is the same phenomenon as resolution-independence of derived functors.** It can look surprising that the function complex does not depend on the frame — frames are far from unique. But this is the model-categorical shadow of a fact every homological algebraist knows: $\mathrm{Ext}$ and $\mathrm{Tor}$ do not depend on the projective resolution chosen. The mechanism is identical — two resolutions of the same object are connected by a weak equivalence between cofibrant objects, and a (right or left) Quillen functor preserves such weak equivalences by **Ken Brown's lemma**. So "the derived mapping space is well-defined" and "$\mathrm{Ext}$ is well-defined" are one theorem in two costumes. Whenever you worry that a homotopical construction depends on a choice of resolution, the resolution is a cofibrant replacement and Ken Brown's lemma is the reason the choice does not matter.

---
type: definition
subject: model-categories
prereqs:
  - "Def - Simplicial Set"
  - "Def - Kan Complex and the Nerve"
  - "Def - Lifting Property and the Retract Argument"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $X, Y, E, B$ are [[Def - Simplicial Set|simplicial sets]], functors $\Delta^{op} \to \mathbf{Set}$, with $n$-simplices $X_n$, face maps $d_i$, degeneracy maps $s_i$. The standard $n$-simplex is $\Delta^n = \Delta(-, [n])$, and the **$k$th horn** $\Lambda^n_k \subseteq \Delta^n$ is the union of all faces of $\Delta^n$ except the $k$th; it is **inner** when $0 < k < n$ and **outer** when $k \in \{0, n\}$. For a class $\mathcal{S}$ of maps, $\mathrm{RLP}(\mathcal{S})$ is the class with the right [[Def - Lifting Property and the Retract Argument|lifting property]] against $\mathcal{S}$, and $\mathrm{LLP}(\mathcal{S})$ the class with the left lifting property. A square commutes and a **lift** is a diagonal filler making both triangles commute. The full registry is on [[Model Categories — The Model Category of Simplicial Sets]].

This is a compound page: it defines two interlocking notions — the **Kan fibration** and the **anodyne extension** — because they are the two halves of a single lifting-complementary pair (the fibrations are the right class, the anodyne maps the left class), and neither is fully usable without the other.

---

# Axiom Motivation

The right way to discover both definitions is to ask: what should a "fibration" of simplicial sets be? In topology a fibration $p : E \to B$ is a map with a *homotopy lifting property* — given a homotopy in the base and a lift of its start, the whole homotopy lifts. The entire art of this chapter is to translate such conditions into the language of horn-filling, because horns are the combinatorial atoms of homotopies. So we want the simplicial condition that says "homotopies lift along $p$".

Recall the [[Def - Kan Complex and the Nerve|Kan complex]]: a simplicial set $X$ in which every horn $\Lambda^n_k \to X$ fills to a simplex $\Delta^n \to X$. The slogan there was *inner-horn fillers are composites* and *outer-horn fillers are inverses*; filling all horns means "compose and invert freely", which is what a space affords. A Kan complex is the absolute version — fillability against the one-point base. The relative version is immediate: a *map* $p : E \to B$ should be a fibration when horns fill *relative to $B$*. Concretely, given a horn $\Lambda^n_k \to E$ in the total space together with a simplex $\Delta^n \to B$ in the base that extends the image of the horn, there should be a filler $\Delta^n \to E$ both extending the horn and lying over the given base simplex. This is exactly the right [[Def - Lifting Property and the Retract Argument|lifting property]] of $p$ against the horn inclusion $\Lambda^n_k \hookrightarrow \Delta^n$. Taking $B = *$ recovers the Kan condition, so the definition is forced by demanding "Kan, but over a base."

Why test *all* horns and not just inner ones? Because we are modelling the homotopy theory of *spaces*, where every path is reversible: a fibration of spaces lifts homotopies in both directions, and the outer horns are exactly the combinatorial content of reversal. If we tested only inner horns we would get a weaker, different notion (an **inner fibration**) appropriate to ∞-categories, where morphisms need not be invertible — that is the Joyal world, not the Kan–Quillen one. The choice "all horns" is the choice "$\infty$-groupoid", and it is what makes the fibre of a Kan fibration a Kan complex.

Now for the second definition. Having declared the fibrations to be $\mathrm{RLP}(\text{horns})$, we ask what the matching *left* class is — the maps that lift on the left against every fibration. These will turn out to be the trivial cofibrations of the model structure, so getting them right is essential. The horn inclusions themselves lift against every Kan fibration (that is the definition of a Kan fibration), but so do many maps built from them. Which ones? Exactly the ones forced by the formal properties of any left lifting class: a map has the left lifting property against a fixed class if it does, and so does any [[Def - Pullback and Pushout|pushout]] of it, any transfinite composite of such, and any retract. So the smallest class of maps that (a) contains the horn inclusions and (b) lifts against every Kan fibration is the *saturation* of the horn inclusions under pushout, transfinite composition, and retract. We call its members **anodyne**. The motivation for the definition is therefore the desire to have an *explicit, constructive* description of the left class — "built from horns" — rather than the *implicit* description "lifts against all fibrations". The theorem that the two descriptions coincide (Gabriel–Zisman) is what makes the model structure checkable.

What breaks if we shrink the saturation operations? Drop closure under **pushout** and the class is far too small — it would not even contain the inclusion of a sub-simplicial-set obtained by attaching a horn-cell, so it would not be closed enough to characterise lifting. Drop closure under **transfinite composition** and you cannot reach infinite-dimensional anodyne maps such as the inclusion of a vertex into an infinite Kan complex built by attaching infinitely many horns; the class would fail to contain genuine trivial cofibrations. Drop closure under **retract** and you lose maps that are summands of horn-composites but not literally built from horns — yet such retracts manifestly still lift against every fibration, so excluding them would make the explicit and implicit descriptions disagree. Each of the three closure operations is exactly one of the formal properties that *any* left lifting class automatically enjoys, so the saturation is the minimal honest candidate, and the content of the subject is that it is also the maximal one.

---

# The Definition

Let $p : E \to B$ be a map of [[Def - Simplicial Set|simplicial sets]].

**Kan fibration.** The map $p$ is a **Kan fibration** if it has the right [[Def - Lifting Property and the Retract Argument|lifting property]] against every horn inclusion: for all $n \ge 1$ and all $0 \le k \le n$, and for every commuting square
$$\begin{array}{ccc} \Lambda^n_k & \xrightarrow{\ a\ } & E \\ \cap & & \downarrow{\scriptstyle p} \\ \Delta^n & \xrightarrow{\ b\ } & B \end{array}$$
there exists a lift $\ell : \Delta^n \to E$ with $\ell|_{\Lambda^n_k} = a$ and $p \circ \ell = b$. Equivalently, $p \in \mathrm{RLP}(\{\Lambda^n_k \hookrightarrow \Delta^n\})$. A simplicial set $X$ is a [[Def - Kan Complex and the Nerve|Kan complex]] precisely when the unique map $X \to *$ is a Kan fibration. A **trivial (acyclic) Kan fibration** is a Kan fibration that is also a weak equivalence; equivalently it has the right lifting property against every *boundary* inclusion $\partial\Delta^n \hookrightarrow \Delta^n$.

**Fibre.** For a vertex $b \in B_0$, regarded as a map $\Delta^0 \to B$, the **fibre** of $p$ over $b$ is the pullback $F_b = E \times_B \Delta^0$, the sub-simplicial-set of $E$ of simplices mapping to the degeneracies of $b$. When $p$ is a Kan fibration, each fibre $F_b$ is a Kan complex.

**Anodyne extension.** The class of **anodyne extensions** is the **saturation** $\overline{J}$ of the set of horn inclusions $J = \{\Lambda^n_k \hookrightarrow \Delta^n : n \ge 1,\ 0 \le k \le n\}$: the smallest class of maps of simplicial sets that contains $J$ and is closed under

1. **pushout** — if $i : A \to A'$ is anodyne and $A \to C$ is any map, the [[Def - Pullback and Pushout|pushout]] $C \to C \cup_A A'$ is anodyne;
2. **transfinite composition** — a (possibly infinite) composite of anodyne maps along a colimit of an ordinal-indexed chain is anodyne;
3. **retract** — a retract of an anodyne map (in the arrow category) is anodyne.

Equivalently — and this is the **Gabriel–Zisman theorem** — the anodyne extensions are exactly the maps with the left lifting property against every Kan fibration: $\overline{J} = \mathrm{LLP}(\{\text{Kan fibrations}\})$. In the model structure they are precisely the trivial cofibrations (monomorphisms that are weak equivalences).

---

# Categorical / Structural Definition

Both notions are instances of the **weak factorisation system** generated by a set. Given any set $J$ of maps in a cocomplete category, write $\mathrm{cell}(J)$ for the transfinite composites of pushouts of maps in $J$, $\mathrm{cof}(J) = \mathrm{LLP}(\mathrm{RLP}(J))$ for the *saturation*, and $\mathrm{inj}(J) = \mathrm{RLP}(J)$ for the injectives. Then $(\mathrm{cof}(J), \mathrm{inj}(J))$ is a weak factorisation system: every map factors as a $\mathrm{cof}(J)$-map followed by an $\mathrm{inj}(J)$-map (by the **small object argument**), and the two classes are lifting-complementary. Specialised to $\mathbf{sSet}$ with $J$ the horn inclusions: $\mathrm{inj}(J) = \{\text{Kan fibrations}\}$ and $\mathrm{cof}(J) = \{\text{anodyne extensions}\}$. So "Kan fibration" and "anodyne extension" are the right and left classes of *the* weak factorisation system cofibrantly generated by the horns.

The structural reason the two descriptions of anodyne maps agree — "built from horns" versus "lifts against fibrations" — is the **retract argument**: if $f = p \circ i$ with $i$ a $\mathrm{cell}(J)$-map and $p \in \mathrm{inj}(J)$, and if $f \in \mathrm{LLP}(\mathrm{inj}(J))$, then $f$ is a retract of $i$, hence in $\mathrm{cof}(J)$ ([[Thm - The Retract Argument]]). This is the categorical mechanism by which an *implicit* lifting class is shown to equal an *explicit* generated class, and it is reused everywhere in cofibrantly generated homotopy theory.

The same template, run with $I = \{\partial\Delta^n \hookrightarrow \Delta^n\}$ in place of $J$, produces the *cofibrations* (monomorphisms, $= \mathrm{cof}(I)$) and the *trivial fibrations* ($= \mathrm{inj}(I)$, the maps with RLP against all boundary inclusions). The two generating sets $I$ and $J$ are the entire input to the [[Thm - Simplicial Sets Form a Model Category|model structure]].

---

# Relate to Other Fields / Compression

A Kan fibration is the combinatorial form of a **Serre fibration**: under [[Thm - Geometric Realization is a Quillen Equivalence|geometric realisation]], Kan fibrations realise to Serre fibrations, and $\mathrm{Sing}$ sends Serre fibrations to Kan fibrations. The homotopy lifting property of topology — lift a homotopy given a lift of its start — becomes, dimension by dimension, the horn-filling lifting property here, because a horn $\Lambda^n_k$ realises to (a retract of) the "homotopy cylinder with one end" and the inclusion into $\Delta^n$ realises to the inclusion of an end into a cylinder. So the relative horn-filling condition *is* the homotopy lifting property, discretised.

The anodyne extensions are the combinatorial form of the **trivial cofibrations** in any cofibrantly generated homotopy theory: the left class generated by the "acyclic cells". In chain complexes the analogue of a horn inclusion is the inclusion of $0$ into a disk complex $D^n$ (an acyclic complex), and the anodyne maps become the trivial cofibrations of the projective model structure; in topological spaces the analogue is $D^n \times \{0\} \hookrightarrow D^n \times [0,1]$, and the anodyne maps become the trivial cofibrations whose pushouts are the mapping cylinders.

**True name:** a Kan fibration is **"a map you can lift homotopies along"**, and an anodyne extension is **"a map built from horns — equivalently, one that lifts against every such fibration"**. When you see "Kan fibration", picture lifting a homotopy from the base; when you see "anodyne", picture either side of the same lifting square — the explicit "assembled from horn-cells" or the implicit "lifts against all fibrations" — and remember that the Gabriel–Zisman theorem is exactly the promise that the two pictures are the same.

---

# Examples / Corollaries

**Is an instance — every Kan complex, as a map to the point.** $X$ is a [[Def - Kan Complex and the Nerve|Kan complex]] if and only if $X \to *$ is a Kan fibration: the square with base $\Delta^n \to *$ is vacuous in the base, so the lifting condition is exactly "every horn $\Lambda^n_k \to X$ fills". Thus Kan fibrations are the relative generalisation of Kan complexes, and the fibrant objects of $\mathbf{sSet}$ are precisely the Kan complexes.

**Is an instance — $\mathrm{Sing}(p)$ for a Serre fibration $p$.** If $p : E \to B$ is a Serre fibration of [[Def - Topological Space|spaces]], then $\mathrm{Sing}(p) : \mathrm{Sing}(E) \to \mathrm{Sing}(B)$ is a Kan fibration. A horn-lifting square for $\mathrm{Sing}(p)$ transposes (across $|{-}| \dashv \mathrm{Sing}$) to a topological lifting problem $|\Lambda^n_k| \to E$, $|\Delta^n| \to B$, which the homotopy lifting property of $p$ solves because $|\Lambda^n_k| \hookrightarrow |\Delta^n|$ is a deformation retract. This is how every topological fibration enters the simplicial world.

**Is an instance — the projection $X \times K \to K$ for $X$ Kan.** If $X$ is a Kan complex then the projection $X \times K \to K$ is a Kan fibration for any $K$: a horn over $K$ lifts because the $X$-coordinate fills by the Kan condition and the $K$-coordinate is supplied by the base. These are the *trivial bundles*, the simplest [[Def - Minimal Fibration|minimal fibrations]].

**Is an instance of anodyne — any horn inclusion, and the inclusion $\{0\} \hookrightarrow \Delta^1$.** Each $\Lambda^n_k \hookrightarrow \Delta^n$ is anodyne by definition. The vertex inclusion $\{0\} = \Delta^0 \hookrightarrow \Delta^1$ is anodyne because it is the horn inclusion $\Lambda^1_0 \hookrightarrow \Delta^1$. More generally the inclusion of either end of the cylinder, $(\partial\Delta^m \times \Delta^1) \cup (\Delta^m \times \{e\}) \hookrightarrow \Delta^m \times \Delta^1$ for $e \in \{0,1\}$, is anodyne — these are the maps that make the homotopy relation work.

**Is NOT a Kan complex — the standard $1$-simplex $\Delta^1$.** The simplicial set $\Delta^1$ (the directed edge $0 \to 1$) is *not* a Kan complex: the outer horn $\Lambda^2_0 \to \Delta^1$ that picks out the edge $0 \to 1$ as the face $d_2$ and a degenerate edge at $0$ as the face $d_1$ has no filler, because a filler would supply an edge $1 \to 0$ inverting $0 \to 1$, which does not exist in $\Delta^1$. So $\Delta^1 \to *$ is *not* a Kan fibration, witnessing that not every simplicial set is fibrant — exactly as $N(\mathcal{C})$ fails to be Kan for a non-groupoid $\mathcal{C}$. (This is also why the [[Def - Quasi-Category|quasi-categories]], which test only inner horns, form a strictly larger class of fibrant objects.)

**Is NOT anodyne — the boundary inclusion $\partial\Delta^n \hookrightarrow \Delta^n$.** Where the *horn* inclusion $\Lambda^n_k \hookrightarrow \Delta^n$ removes one face (and the interior) and is anodyne, the *boundary* inclusion $\partial\Delta^n \hookrightarrow \Delta^n$ removes only the interior, keeps all $n+1$ faces, and is *not* anodyne: it is a monomorphism (so a cofibration) but not a weak equivalence — its realisation $S^{n-1} \hookrightarrow D^n$ is not a homotopy equivalence — so it is a non-trivial cofibration whose pushouts attach cells that change homotopy type. The difference of a single face is the difference between "trivial cofibration" and "cofibration": all anodyne maps are monomorphisms, but most monomorphisms are not anodyne.

**Corollary — Kan fibrations are closed under pullback, composition, and retract.** Right lifting classes always are: a [[Def - Pullback and Pushout|pullback]] of a Kan fibration is a Kan fibration (lift in the pullback by lifting in the original and using the universal property), and composites and retracts of Kan fibrations are Kan fibrations. Dually, anodyne maps are closed under pushout, transfinite composition, and retract — by definition.

**Corollary — the fibre of a Kan fibration is a Kan complex.** If $p : E \to B$ is a Kan fibration and $F_b$ is the fibre over a vertex $b$, then $F_b \to *$ is the pullback of $p$ along $* \to B$, hence a Kan fibration; so $F_b$ is a Kan complex. This is what makes the [[Def - Simplicial Homotopy Group|homotopy groups of the fibre]] well-defined and the long exact sequence available.

**Calibration check.** Verify that $X \to *$ being a Kan fibration unwinds to the horn-filling definition of a Kan complex. Confirm that a pullback of a Kan fibration is a Kan fibration by a one-line diagram chase. And explain why each of the three closure operations (pushout, transfinite composition, retract) is automatically enjoyed by *any* class of the form $\mathrm{LLP}(\mathcal{S})$ — this is exactly the reason the anodyne class is defined by those three operations.

---

# Unlocked by This

> [!tip] The Model Structure on Simplicial Sets *(from this chapter)*
> With Kan fibrations as the fibrations and anodyne extensions as the trivial cofibrations, [[Thm - Simplicial Sets Form a Model Category]] verifies Quillen's axioms; the two factorisations come from the small object argument applied to the horn inclusions $J$ and the boundary inclusions $I$. This definition is the fibration half of the model structure.

> [!tip] Simplicial Homotopy Groups and the Long Exact Sequence *(from this chapter)*
> Because the fibre of a Kan fibration is a Kan complex, the [[Def - Simplicial Homotopy Group|simplicial homotopy groups]] of fibre, total space, and base fit into a long exact sequence $\dots \to \pi_n F \to \pi_n E \to \pi_n B \to \pi_{n-1} F \to \dots$, the combinatorial form of the homotopy long exact sequence of a fibration.

> [!tip] Inner Fibrations and the Joyal Model Structure *(from Higher Category Theory)*
> Testing only *inner* horns gives an **inner fibration**, and the corresponding model structure (same cofibrations, [[Def - Quasi-Category|quasi-categories]] as fibrant objects) is the **Joyal model structure** presenting the homotopy theory of ∞-categories. The Kan–Quillen fibrations are the inner fibrations that also lift outer horns — the "left and right fibrations" combined.

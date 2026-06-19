---
type: definition
subject: model-categories
prereqs:
  - "Def - Limit and Colimit"
  - "Def - Pullback and Pushout"
  - "Def - Lifting Property and the Retract Argument"
  - "Def - Functor"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a category, $\mathcal{W}$ is its class of **weak equivalences** (written $\xrightarrow{\sim}$), and we have classes of **cofibrations** (written $\rightarrowtail$) and **fibrations** (written $\twoheadrightarrow$). A map that is both a cofibration and a weak equivalence is a **trivial cofibration** (or **acyclic cofibration**); a map that is both a fibration and a weak equivalence is a **trivial fibration**. The symbols $\varnothing$ and $*$ denote the initial and terminal objects, which exist because $\mathcal{M}$ is bicomplete. We say $i$ has the **left lifting property** (LLP) against $p$, and $p$ has the **right lifting property** (RLP) against $i$, when every commuting square with $i$ on the left and $p$ on the right has a diagonal filler — see [[Def - Lifting Property and the Retract Argument]] for the precise diagram. The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

We present the classical **Quillen axioms MC1–MC5** as the primary formulation, since they are cleaner pedagogically, and then note Hovey's functorial-factorization refinement.

---

# Axiom Motivation

The right way to discover this definition is to want one specific thing: to *invert* a class of maps and have the result be computable. Suppose you are doing topology and you have decided that what matters is not homeomorphism but **weak homotopy equivalence** — a map $f : X \to Y$ inducing an isomorphism on every [[Def - Higher Homotopy Group|homotopy group]] $\pi_n$. You want a category in which all such $f$ are isomorphisms. Abstractly this category exists: it is the localization $\mathbf{Top}[\mathcal{W}^{-1}]$, the universal recipient of a functor inverting $\mathcal{W}$. But it is useless as given, because a morphism in it is an equivalence class of zig-zags $X \leftarrow \bullet \to \bullet \leftarrow \cdots \to Y$, and you cannot compute with those — you cannot even guarantee the morphisms form a set. The question that forces the entire definition is: *what extra structure makes this localization computable?*

Quillen's answer is to add two more classes of maps, cofibrations and fibrations, and to impose axioms forcing them to interlock with $\mathcal{W}$. The desideratum each axiom serves is concrete, and the surest way to see that the list is not arbitrary is to drop axioms one at a time and watch a named construction collapse.

**Why bicompleteness (MC1).** You need all small limits and colimits because the constructions of the theory are built from them: the cylinder object is a colimit (a factored coproduct), the path object a limit, and (co)fibrant replacements come from factoring the maps $\varnothing \to X$ and $X \to *$, which require the initial and terminal objects to exist in the first place. Drop completeness and you cannot even form the diagonal $X \to X \times X$ that defines a path object; drop cocompleteness and there is no fold map $A \sqcup A \to A$ to factor into a cylinder. Quillen originally required only *finite* limits and colimits, but every example he met sat inside a bicomplete category, and the small object argument that builds factorizations needs transfinite colimits, so the modern convention demands all small ones.

**Why 2-out-of-3 (MC2).** This says: if two of $f$, $g$, $g \circ f$ are weak equivalences, so is the third. The desideratum is that "weak equivalence" behave like "isomorphism," and isomorphisms satisfy 2-out-of-3. If you drop it, the homotopy relation on maps stops being transitive. Here is the mechanism: transitivity of left homotopy is proved by gluing two cylinders end to end and certifying that the glued object is again a cylinder, and the certification — that the new structure map is a weak equivalence — is a 2-out-of-3 argument. Without MC2 you can have $f \simeq g$ and $g \simeq h$ with $f \not\simeq h$, and then "homotopy classes of maps" is not even a well-defined set of equivalence classes, so the homotopy category cannot be described as in the fundamental theorem. MC2 is what makes weak equivalences composable into a coherent notion of "the same."

**Why retracts (MC3).** Each of the three classes must be closed under retracts: if $f$ is a retract of $g$ (it sits inside $g$ via a retract diagram) and $g$ is a weak equivalence, cofibration, or fibration, then so is $f$. The desideratum is that the classes be detectable by lifting properties, and a class defined by a lifting property is *automatically* closed under retracts — so demanding retract-closure is demanding consistency with the lifting axiom. Drop it and the lifting characterization of the classes (a cofibration is exactly a map with LLP against trivial fibrations) fails, because the retract argument — the proof that "lifts against the right class" implies "belongs to the class" — depends on retract-closure to conclude. In Hovey's formulation MC3 is essentially the *only* axiom beyond the structure, and lifting and factorization become theorems; that is the precise sense in which retract-closure is the load-bearing closure condition.

**Why lifting (MC4).** This is the heart. It says trivial cofibrations have the LLP against fibrations, and cofibrations have the LLP against trivial fibrations. The desideratum is the ability to *construct maps* — homotopies, comparison maps, retractions — by filling in diagonals of squares. Every homotopy in the theory is literally a lift: a left homotopy $\mathrm{Cyl}(A) \to B$ is constructed by lifting against a fibration. Drop MC4 and you cannot build a single homotopy or comparison map; cofibrant replacements would exist (from MC5) but you could not compare two of them, so the homotopy category would have no well-defined morphisms. Lifting is the axiom that lets the scaffolding actually carry weight.

**Why factorization (MC5).** Every map $f$ must factor two ways: as a cofibration followed by a trivial fibration, and as a trivial cofibration followed by a fibration. The desideratum is **(co)fibrant replacement**: factor $\varnothing \to X$ to get a cofibrant $QX \xrightarrow{\sim} X$, factor $X \to *$ to get a fibrant $X \xrightarrow{\sim} RX$. Drop MC5 and there are no replacements, so you cannot compute the homotopy category (whose morphisms are homotopy classes of maps between *bifibrant* replacements) and derived functors do not exist (since $\mathbf{L}F = F \circ Q$ needs $Q$). MC5 is what guarantees enough good objects to do everything on.

A reader who internalizes "each axiom is necessary for one named feature — transitivity of homotopy, construction of homotopies, (co)fibrant replacement" could reinvent the definition by asking what is minimally needed to make localization computable. That is the test of a good axiom motivation, and these five pass it.

---

# The Definition

A **model category** is a category $\mathcal{M}$ together with three classes of morphisms — **weak equivalences** $\mathcal{W}$, **cofibrations**, and **fibrations**, each closed under composition and containing all identities — satisfying the following five axioms. A **trivial** (acyclic) cofibration is a map that is both a cofibration and a weak equivalence; a **trivial fibration** is both a fibration and a weak equivalence.

> **(MC1) Limits and colimits.** $\mathcal{M}$ has all small limits and colimits (it is bicomplete). In particular it has an initial object $\varnothing$ and a terminal object $*$.

> **(MC2) Two-out-of-three.** If $f$ and $g$ are composable morphisms and two of $f$, $g$, $g \circ f$ are weak equivalences, then so is the third.

> **(MC3) Retracts.** If $f$ is a retract of $g$ and $g$ is a weak equivalence, a cofibration, or a fibration, then $f$ is also a weak equivalence, a cofibration, or a fibration respectively.

> **(MC4) Lifting.** In any commuting square
> $$\begin{array}{ccc} A & \longrightarrow & X \\ \scriptstyle i \downarrow & & \downarrow \scriptstyle p \\ B & \longrightarrow & Y \end{array}$$
> a diagonal lift $h : B \to X$ exists (with $h \circ i$ equal to the top map and $p \circ h$ equal to the bottom map) in either of two cases: $i$ is a cofibration and $p$ is a trivial fibration, or $i$ is a trivial cofibration and $p$ is a fibration.

> **(MC5) Factorization.** Every morphism $f$ has two factorizations: $f = p \circ i$ with $i$ a cofibration and $p$ a trivial fibration; and $f = q \circ j$ with $j$ a trivial cofibration and $q$ a fibration.

A model category is bicomplete by MC1, and one habitually abuses language by calling $\mathcal{M}$ "a model category," leaving the three classes implicit.

**Hovey's refinement.** Hovey (and Kan before him) sharpens MC5 to demand *functorial* factorizations — an ordered pair of functors $(\alpha, \beta)$ on the arrow category with $f = \beta(f) \circ \alpha(f)$ — and weakens the rest of the package to require only MC2, MC3, and the existence of the two functorial factorizations, *plus* the two lifting properties phrased so that closure becomes provable. In Hovey's setup the lifting axiom MC4 and the closure properties of [[Thm - Closure Properties of the Model Structure]] are **theorems**, derived from the retract axiom and functoriality via [[Thm - The Retract Argument]]. Functoriality matters because it makes (co)fibrant replacement a genuine functor and the comparison maps natural — essential when one wants maps of model categories to behave well. For learning the subject, the classical MC1–MC5 are cleaner; for the technical development, Hovey's are tighter.

---

# Categorical / Structural Definition

The cleanest structural packaging is through **weak factorization systems**. A weak factorization system on $\mathcal{M}$ is a pair $(\mathcal{L}, \mathcal{R})$ of classes of maps such that every map factors as a map of $\mathcal{L}$ followed by a map of $\mathcal{R}$, the class $\mathcal{L}$ is exactly the maps with the LLP against all of $\mathcal{R}$, and $\mathcal{R}$ is exactly the maps with RLP against all of $\mathcal{L}$. From this vantage, a model structure is precisely **two weak factorization systems sharing a class**: the pair (cofibrations, trivial fibrations) and the pair (trivial cofibrations, fibrations), tied together by the single class $\mathcal{W}$ via the rule that a cofibration is trivial exactly when it lies in $\mathcal{W}$, and likewise for fibrations, with $\mathcal{W}$ satisfying 2-out-of-3 and closed under retracts. This is the form in which [[Thm - Closure Properties of the Model Structure|the closure theorem]] is most transparent: the lifting characterizations of the four classes are exactly the defining property of a weak factorization system.

There is a deeper structural reading. The data $(\mathcal{M}, \mathcal{W})$ alone — a category with a distinguished class of equivalences — is a **relative category**, and its homotopy theory is a presentation of an **(∞,1)-category**, namely the result of inverting $\mathcal{W}$ in the homotopy-coherent sense. A model structure is then a choice of cofibrations and fibrations that *computes* this (∞,1)-category: it identifies the cofibrant and fibrant objects on which the abstract localization reduces to concrete homotopy classes. Two model structures with the same $\mathcal{W}$ present the same (∞,1)-category, and a Quillen equivalence is the statement that two presentations agree — this is made precise in [[Def - Quillen Adjunction and Quillen Equivalence]] and [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]].

---

# Relate to Other Fields / Compression

A model category is to homotopy theory what a basis is to a vector space: a *presentation* that makes an intrinsic object computable, not part of the object itself. The intrinsic object is the homotopy theory $(\mathcal{M}, \mathcal{W})$; the cofibrations and fibrations are the basis-like choice that lets you write things down. Just as different bases present the same space and are related by change of coordinates, different model structures with the same weak equivalences present the same homotopy theory and are related by Quillen equivalences.

The most precise compression is into homological algebra, where the analogy is an identity. The construction of the **derived category** $D(R)$ — invert quasi-isomorphisms in chain complexes — is the exact problem this definition solves, with $\mathbf{Ch}(R)$ as $\mathcal{M}$ and quasi-isomorphisms as $\mathcal{W}$. Cofibrant objects are complexes of projectives, the homotopy relation is [[Def - Chain Map and Chain Homotopy|chain homotopy]], and derived functors like $\mathbf{Tor}$ are the total derived functors of the model structure. So "model category" is the common generalization of "the homotopy category of spaces" and "the derived category of an abelian category" — the two historical sources of the subject, unified.

**True name:** a model category is **a relative category $(\mathcal{M}, \mathcal{W})$ together with a computational scaffolding (cofibrations and fibrations) that makes localization at $\mathcal{W}$ tractable.** When you reach for the structure, you are reaching for the ability to replace objects by good ones and to construct maps by lifting — the cofibrations and fibrations are means, the homotopy category is the end.

---

# Examples / Corollaries

**Is an instance — $\mathbf{Top}$, the Quillen model structure.** Take weak equivalences to be the [[Def - Higher Homotopy Group|weak homotopy equivalences]], fibrations the Serre fibrations (maps with the homotopy lifting property against all disks $D^n$), and cofibrations the retracts of relative cell complexes. Every space is fibrant (the map $X \to *$ is always a Serre fibration), the cofibrant objects are the CW-like spaces, and the factorizations come from the small object argument applied to the generating cofibrations $S^{n-1} \hookrightarrow D^n$. The homotopy category is the classical homotopy category of CW complexes.

**Is an instance — $\mathbf{Ch}(R)$, the projective model structure.** On chain complexes of [[Def - Module|modules]] over a ring $R$, take weak equivalences to be quasi-isomorphisms, fibrations the degreewise surjections, and cofibrations the monomorphisms with degreewise-projective cokernel. Cofibrant objects are the bounded-below complexes of projectives, the homotopy relation is chain homotopy, and the homotopy category is the derived category $D(R)$.

**Is an instance — $\mathbf{sSet}$, the Kan–Quillen model structure.** On [[Def - Simplicial Set|simplicial sets]], cofibrations are the monomorphisms, fibrations the Kan fibrations, and weak equivalences the maps that become weak homotopy equivalences after [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|geometric realization]]. Every object is cofibrant; the fibrant objects are the [[Def - Kan Complex and the Nerve|Kan complexes]].

**Is an instance — the trivial model structures.** On any bicomplete $\mathcal{C}$, setting $\mathcal{W}$ = the isomorphisms and both other classes = all maps gives a model structure (the lifting and factorization axioms are then nearly content-free); its homotopy category is $\mathcal{C}$ itself. See [[Ex - The trivial model structures on a category]].

**Is NOT an instance — a category with $\mathcal{W}$ failing 2-out-of-3.** Take any category and declare a class $\mathcal{W}$ that is not closed under the 2-out-of-3 rule — say, on a three-object chain $A \xrightarrow{f} B \xrightarrow{g} C$, declaring $f$ and $g \circ f$ weak equivalences but not $g$. No choice of cofibrations and fibrations can repair this: MC2 is violated outright, so there is no model structure with these weak equivalences. This shows the weak equivalences are not free data — they must already behave like equivalences.

**Is NOT an instance — a poset (in general).** A non-trivial poset, viewed as a category, is not bicomplete unless it is a complete lattice, so MC1 already fails; and even a complete lattice carries only trivial homotopy theory, since the only candidate weak equivalences are identities. Posets are too rigid: there is no room for the "deformation" that homotopy theory is about.

**Calibration check.** Verify that in any model category every isomorphism is simultaneously a trivial cofibration and a trivial fibration (use MC3 with the retract diagram exhibiting an isomorphism as a retract of an identity, or check it lifts both ways). Verify that the initial object $\varnothing$ is cofibrant and the terminal object $*$ is fibrant directly from the definitions in [[Def - Cofibrant and Fibrant Objects]]. If you can also state which axiom guarantees that the cylinder object $\mathrm{Cyl}(A)$ exists — it is MC1 (the coproduct $A \sqcup A$) together with MC5 (the factorization of the fold map) — you have understood how the axioms cooperate.

---

# Unlocked by This

> [!tip] The Homotopy Category and the Derived Category *(from this chapter)*
> With the axioms in hand, [[Thm - The Homotopy Category of a Model Category]] constructs $\mathrm{Ho}(\mathcal{M})$ as bifibrant objects and homotopy classes, and specializing to $\mathbf{Ch}(R)$ yields the **derived category** $D(R)$. Every "derived" construction in mathematics is an instance.

> [!tip] Stable Homotopy Theory and Spectra *(from Algebraic Topology)*
> Imposing the model-category axioms on a category of **spectra** and inverting the stable equivalences produces the **stable homotopy category**, where suspension is invertible. The same five axioms govern it; the new feature is stability, which makes the homotopy category **triangulated**.

> [!tip] ∞-Categories and the Homotopy Hypothesis *(from Higher Category Theory)*
> A model category presents an **(∞,1)-category**; the Kan–Quillen structure on $\mathbf{sSet}$ presents the (∞,1)-category of spaces, and its Quillen equivalence with $\mathbf{Top}$ is a rigorous form of the **homotopy hypothesis**. Model categories are the bridge from 1-categorical foundations to the [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories|Higher Categories]] world.

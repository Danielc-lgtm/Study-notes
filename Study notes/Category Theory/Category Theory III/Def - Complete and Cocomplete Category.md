---
type: definition
subject: category-theory
prereqs:
  - "Def - Limit and Colimit"
  - "Def - Product and Coproduct"
  - "Def - Equalizer and Coequalizer"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]]. A diagram $D : J \to \mathcal{C}$ is **small** if its index category $J$ is small (its objects and morphisms form sets, not proper classes); it is **finite** if $J$ has finitely many objects and morphisms. We write $\lim D$, $\operatorname{colim} D$ for [[Def - Limit and Colimit|limit and colimit]]. The named categories are $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Ab}$, $\mathbf{Ring}$, $\mathbf{CRing}$, $\mathbf{Mod}_R$, $\mathbf{Vect}_k$, $\mathbf{Top}$, $\mathbf{Cat}$. The full registry is on [[Category Theory III — Limits and Colimits]].

This is a compound page: it defines the dual pair **complete** and **cocomplete** together, since cocompleteness of $\mathcal{C}$ is completeness of $\mathcal{C}^{op}$.

---

# Axiom Motivation

Once you can take the [[Def - Limit and Colimit|limit]] of an individual diagram, the natural next question is structural: does a given category have *enough* limits to do business? "Enough" turns out to mean "all small ones", and the reason the cutoff is at *small* (rather than *all*) diagrams is forced by a genuine theorem, not by timidity. A category with limits of diagrams as large as the category itself is necessarily a [[Def - Category|preorder]] (Freyd's theorem) — so demanding *all* limits collapses the notion to triviality, while demanding all *small* limits is exactly the right amount: every diagram you index by an honest set of vertices and edges can be resolved.

So define $\mathcal{C}$ to be **complete** if every small diagram has a limit, and **cocomplete** if every small diagram has a colimit. The desideratum behind this is that completeness should let you *build* objects by universal constructions without leaving the category: form products, cut out subobjects by equalizers, take fibre products, assemble inverse limits — all of these stay inside a complete category. A working category should be a place where the constructions of mathematics can be carried out, and completeness is the precise statement that they can.

The single most useful fact, and the reason completeness is checkable rather than an infinite list of obligations, is a *reduction*: a category is complete if and only if it has **all small products and all equalizers** (equivalently, all small products and all [[Def - Pullback and Pushout|pullbacks]], or all products and a terminal object and pullbacks). You do not verify limits of every shape separately; you verify two kinds of limit and get the rest for free, because every limit is the equalizer of a pair of maps between products (see [[Thm - Products and Equalizers Give All Limits]]). Dually, cocompleteness reduces to coproducts and coequalizers. This is what makes "$\mathbf{Set}$ is complete and cocomplete" a finite verification.

It is worth separating **finite** completeness from completeness, because the distinction is load-bearing downstream. A category is **finitely complete** (has all finite limits) if and only if it has finite products and equalizers, equivalently a terminal object and pullbacks. Finite completeness is the hypothesis for **cartesian** structure, for the internal logic of a category, and for the definition of many notions (e.g. internal groups, **topos** axioms ask for finite limits). Full completeness adds infinite products, which is what is needed for the adjoint functor theorem and for inverse limits. Keeping the two apart tells you exactly how much structure a given argument requires.

What would go wrong if a category were *not* complete? You would be unable to perform a basic construction inside it and would be forced out. The category of *finite* sets has all finite limits but not all small products (an infinite product of finite sets need not be finite), so it is finitely complete but not complete — and any construction needing an infinite product escapes to $\mathbf{Set}$. The category of fields lacks even binary products. Recognising which constructions a category supports is exactly recognising its completeness.

---

# The Definition

A category $\mathcal{C}$ is **complete** if every small diagram $D : J \to \mathcal{C}$ (with $J$ small) has a limit in $\mathcal{C}$. It is **cocomplete** if every small diagram has a colimit.

$\mathcal{C}$ is **finitely complete** (or has **finite limits**, or is **left exact / lex / cartesian**) if every finite diagram has a limit; **finitely cocomplete** if every finite diagram has a colimit.

The completeness conditions admit the following equivalent criteria (proved in [[Thm - Products and Equalizers Give All Limits]]):

- $\mathcal{C}$ is **complete** $\iff$ $\mathcal{C}$ has all small [[Def - Product and Coproduct|products]] and all [[Def - Equalizer and Coequalizer|equalizers]] $\iff$ $\mathcal{C}$ has all small products and all [[Def - Pullback and Pushout|pullbacks]].
- $\mathcal{C}$ is **finitely complete** $\iff$ $\mathcal{C}$ has finite products and equalizers $\iff$ $\mathcal{C}$ has a [[Def - Initial and Terminal Object|terminal object]] and all pullbacks.
- Dually, **cocomplete** $\iff$ all small coproducts and all coequalizers; **finitely cocomplete** $\iff$ finite coproducts and coequalizers $\iff$ initial object and all pushouts.

A category that is both complete and cocomplete is called **bicomplete**.

---

# Relate to Other Fields / Compression

Completeness is the categorical generalisation of "a complete lattice" and of "a space where you can take limits". A [[Def - Category|poset viewed as a category]] is complete (and cocomplete) as a category if and only if it is a **complete lattice** — every subset has an infimum (its product/limit) and a supremum (its coproduct/colimit). So the completeness of the powerset lattice, of the lattice of subgroups, of the closed sets of a topology, are all instances of categorical completeness. In analysis, the existence of inverse limits (Cauchy completions, profinite groups) is a completeness statement.

**True name:** a complete category is "one where every universal construction with set-many constraints has a solution inside the category". The operational test is never "check all diagrams" — it is **"does it have all products and all equalizers?"**, and the dual for cocompleteness.

---

# Examples / Corollaries

**Is an instance — $\mathbf{Set}$ is complete and cocomplete.** Products are cartesian products, equalizers are agreement-subsets, so $\mathbf{Set}$ has all small limits; coproducts are disjoint unions, coequalizers are quotients by generated equivalence relations, so it has all small colimits. Every limit is computed as a subset of a product (compatible families) and every colimit as a quotient of a coproduct. See [[Ex - Set is complete and cocomplete]].

**Is an instance — the algebraic categories $\mathbf{Grp}, \mathbf{Ab}, \mathbf{Ring}, \mathbf{Mod}_R, \mathbf{Vect}_k$ are complete and cocomplete.** Their limits are computed on underlying sets (the [[Def - Preservation, Reflection, and Creation of Limits|forgetful functor creates limits]]): a product of groups is the [[Def - Direct Product|direct product]] with the unique compatible group structure, an equalizer is the subgroup where two homomorphisms agree. Colimits are subtler — the coproduct in $\mathbf{Grp}$ is the [[Def - Free Group and Free Product|free product]], not the disjoint union — but they exist. $\mathbf{Top}$ is also bicomplete: limits get the coarsest topology making the legs continuous, colimits the finest.

**Is an instance — $\mathbf{Cat}$ is complete and cocomplete.** Limits of categories are computed on objects and morphisms (the product category, the equalizer subcategory); colimits exist but are more delicate. This is what lets one speak of pullbacks and products *of categories themselves*.

**Is NOT an instance — finite sets and finite-dimensional vector spaces are only finitely (co)complete.** $\mathbf{FinSet}$ has all finite limits and colimits but not infinite products: $\prod_{n \in \mathbb{N}} \{0,1\}$ is uncountable, not finite. Likewise $\mathbf{FinVect}_k$ has finite biproducts but not infinite products. They are finitely bicomplete, not bicomplete — the cutoff at "finite" is essential.

**Is NOT an instance — $\mathbf{Field}$ is not even finitely complete.** The category of fields lacks binary products (as objects $\mathbb{Q} \times \mathbb{F}_2$ is not a field) and lacks an initial object that works for all characteristics, so it fails finite completeness outright. This is the standard cautionary example: not every familiar category supports limits, and $\mathbf{Field}$ is the one to remember.

**Calibration check.** Verify that a complete category has a terminal object (the empty product) and a cocomplete one has an initial object. Check that a poset is complete as a category exactly when it is a complete lattice, by matching infima to products. If you can explain why "complete" requires only products-and-equalizers rather than a separate check for pullbacks and inverse limits, you have understood the reduction.

---

# Unlocked by This

> [!tip] Locally Presentable and Accessible Categories *(from Categorical Logic)*
> A **locally presentable category** is a cocomplete category generated under filtered colimits by a set of small objects; these are exactly the categories of models of limit/colimit theories, and the setting where the adjoint functor theorems hold cleanly. Completeness/cocompleteness is the load-bearing hypothesis.

> [!tip] Grothendieck Topoi and Sheaves *(from Topos Theory and Algebraic Geometry)*
> A **Grothendieck topos** — a category of **sheaves** on a site — is complete and cocomplete, with limits computed pointwise as in any **presheaf** category and colimits computed by sheafifying the presheaf colimit. Bicompleteness is one of the Giraud axioms characterising topoi, and is what makes them a place to do geometry and logic.

> [!tip] Model Categories *(from Chapter VI)*
> A **model category** is required to be (at least finitely) complete and cocomplete, so that the lifting and factorization axioms have the limits and colimits they need. Completeness is a standing background hypothesis for the entire homotopy-theoretic machinery.

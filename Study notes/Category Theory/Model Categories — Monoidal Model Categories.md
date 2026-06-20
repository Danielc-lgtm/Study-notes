---
type: topic
subject: model-categories
chapter: "Hovey Ch4"
title: "Model Categories — Monoidal Model Categories"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation Registry

This chapter sits at the intersection of two structures: the **monoidal** structure of [[Category Theory V — Monads, Algebras, and Monoidal Categories]] and the **model** structure of [[Model Categories — Quillen's Axiomatization of Homotopy Theory]]. We assume the monoidal product is **closed** (it has an internal hom) and, by default, **symmetric** — Hovey works with closed symmetric monoidal categories throughout, and so do we, flagging explicitly where symmetry is genuinely used rather than convenient. The single most important convention is that **the tensor product on the homotopy category is the *derived* tensor, never the naive one**: $\otimes$ on $\mathcal{C}$ does not descend to $\mathrm{Ho}(\mathcal{C})$, but $\otimes^{\mathbf{L}}$ — tensor *after cofibrant replacement* — does. Whenever a tensor appears on a homotopy category in this chapter it is the derived one.

- $\mathcal{C}, \mathcal{D}, \mathcal{E}$ — categories; $\mathcal{C}$ is the ambient (closed symmetric monoidal model) category
- $\otimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$ — the monoidal product (tensor); $A \otimes B$ on objects, $f \otimes g$ on morphisms
- $I$ — the **unit object** of the monoidal structure (often $\mathbb{1}$, $S^0$, $R$, or $\Delta^0$ in examples)
- $[B, C]$ or $\underline{\mathrm{Hom}}(B, C)$ — the **internal hom**: the object of maps $B \to C$, right adjoint to $- \otimes B$
- $\alpha_{A,B,C}, \lambda_A, \rho_A$ — associator and unitors of the monoidal structure
- $\mathrm{ev} : [B, C] \otimes B \to C$ — **evaluation**, the counit of $- \otimes B \dashv [B, -]$
- $\mathcal{W}$, $\rightarrowtail$, $\twoheadrightarrow$, $\xrightarrow{\sim}$ — weak equivalences, cofibrations, fibrations, weak equivalence
- $f \mathbin{\square} g$ — the **pushout-product** of $f$ and $g$ (also written $f \,\hat\otimes\, g$)
- $\langle f, p\rangle$ or $[i, p]$ — the **pullback-hom** (Leibniz cotensor) of a map $i$ and a map $p$
- $Q$, $R$ — cofibrant and fibrant replacement functors; $QX \xrightarrow{\sim} X$, $X \xrightarrow{\sim} RX$
- $\otimes^{\mathbf{L}}$ — the **derived tensor product**, $A \otimes^{\mathbf{L}} B := QA \otimes QB$ (computed in $\mathrm{Ho}(\mathcal{C})$)
- $\mathrm{Ho}(\mathcal{C})$ — the homotopy category $\mathcal{C}[\mathcal{W}^{-1}]$
- $\mathbf{Ch}(R)$ — chain complexes of $R$-modules; $\otimes_R$ its tensor product
- $\mathbf{sSet}$ — simplicial sets; $\Delta^n$ the standard $n$-simplex; $\times$ the cartesian product
- $A_\bullet \wedge B_\bullet$, $\mathbb{S}$ — smash product of symmetric spectra and the sphere spectrum
- $\mathbf{Mod}_R$ — modules over a monoid $R$ in $\mathcal{C}$
- $\mathrm{Tor}^R_*$, $\mathrm{Ext}_R^*$ — the derived functors of $\otimes_R$ and $\mathrm{Hom}_R$

---

# Motivation

Here is the entire chapter in one sentence: a monoidal model category is the minimal setting in which a tensor product survives the passage to homotopy. You have already built two great machines. One is the **monoidal category** — a category with a tensor product $\otimes$, a unit $I$, and coherent associativity and unit isomorphisms, the abstraction of "multiplying objects". The other is the **model category** — a category with weak equivalences, cofibrations, and fibrations, the abstraction of "doing homotopy theory". The natural question is what happens when a single category carries both, and the answer is not automatic, because the two structures fight.

The fight is concrete and you have seen it before, in homological algebra. Take $\mathcal{C} = \mathbf{Ch}(R)$, the chain complexes over a ring, with its tensor product $\otimes_R$ and its quasi-isomorphisms as weak equivalences. The naive tensor product is *not* homotopy-invariant: replacing a complex by a quasi-isomorphic one can change $M \otimes_R N$ up to quasi-isomorphism. The classic witness is $\mathbb{Z}/2 \otimes_{\mathbb{Z}} \mathbb{Z}/2$. The complex $\mathbb{Z}/2$ (in degree zero) is quasi-isomorphic to its projective resolution $[\,\mathbb{Z} \xrightarrow{2} \mathbb{Z}\,]$, but tensoring the resolution with $\mathbb{Z}/2$ gives $[\,\mathbb{Z}/2 \xrightarrow{0} \mathbb{Z}/2\,]$, whose homology is $\mathbb{Z}/2$ in *two* degrees, not one. The discrepancy in the degree-one homology is exactly $\mathrm{Tor}^{\mathbb{Z}}_1(\mathbb{Z}/2, \mathbb{Z}/2) = \mathbb{Z}/2$. So $\otimes_R$ does not descend to a functor on the derived category; what descends is the *derived* tensor $\otimes^{\mathbf{L}}_R$, computed by first replacing one factor by a complex of projectives. Tor is the obstruction to the naive tensor being homotopy-invariant, and the derived tensor is the repair.

The whole subject of this chapter is the recognition that this is not a quirk of chain complexes but a general phenomenon, and that one short axiom controls it. The phenomenon is: $\otimes$ rarely preserves weak equivalences, so it cannot descend to $\mathrm{Ho}(\mathcal{C})$ as it stands; but if $\otimes$ interacts correctly with the cofibrations, then tensoring *cofibrant* objects is homotopy-invariant, and the **derived tensor** $\otimes^{\mathbf{L}}$ — tensor after cofibrant replacement — makes $\mathrm{Ho}(\mathcal{C})$ into a monoidal category. The one short axiom is the **pushout-product axiom** (Quillen's "SM7"), which demands that the pushout-product of two cofibrations be a cofibration, trivial whenever either factor is. A second, smaller condition — the **unit axiom** — patches up the corner case where the unit object $I$ is not itself cofibrant. The payoff is the structural backbone of the chapter:

$$\big(\mathcal{C}, \otimes, I\big) \ \text{closed monoidal model} \quad\Longrightarrow\quad \big(\mathrm{Ho}(\mathcal{C}), \otimes^{\mathbf{L}}, QI\big) \ \text{closed monoidal}.$$

Once you have this, an enormous amount follows for free. The smash-product on the stable homotopy category, the derived tensor on the derived category $D(R)$, the cartesian product on the homotopy category of spaces — these are all instances of one theorem. Better still, the pushout-product is one half of a *two-variable* adjunction, and its right adjoint, the **pullback-hom**, controls when the internal hom is homotopy-invariant. The pair $(\square, \text{pullback-hom})$ forms a **Quillen bifunctor**, the homotopical refinement of a closed monoidal structure, and from it both the derived tensor and the derived internal hom drop out simultaneously. Finally, once tensoring is homotopically sound, one can do *algebra* in $\mathcal{C}$: monoids in $\mathcal{C}$ are "rings up to homotopy", and **modules** over them inherit a model structure of their own, which is where ring spectra, $E_\infty$-algebras, and the modern foundations of stable homotopy theory live.

This chapter assumes you are fluent in model categories — the axioms, lifting and factorization, the homotopy category, cofibrant and fibrant replacement, and Quillen adjunctions (all of [[Model Categories — Quillen's Axiomatization of Homotopy Theory]]) — and in monoidal categories — tensor, unit, associator, the symmetric case, internal hom (the relevant parts of [[Category Theory V — Monads, Algebras, and Monoidal Categories]] and [[Category Theory IV — Adjunctions]]). You should also have the derived tensor product and Tor from homological algebra at hand, since they are the running example. If "Ken Brown's lemma" and "cofibrant replacement" are not immediately meaningful, refresh those before proceeding.

---

# Concept Map

## §1 Closed Monoidal Categories and Modules

- **[[Def - Closed Monoidal Category]]**
	- A **closed monoidal category** is a monoidal category $(\mathcal{C}, \otimes, I)$ in which every functor $- \otimes B$ has a right adjoint $[B, -]$, the **internal hom**, so $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C])$ naturally. It is the abstraction of "the maps $B \to C$ form an object of $\mathcal{C}$ again", with $\mathrm{ev} : [B, C] \otimes B \to C$ the counit and currying the transpose. The cartesian case ($\otimes = \times$) is exactly a [[Def - Cartesian Closed Category|cartesian closed category]]; the non-cartesian template is $\mathbf{Mod}_R$ with $- \otimes_R M \dashv \mathrm{Hom}_R(M, -)$, which is closed but not cartesian closed. Closedness is what lets us state the pushout-product axiom's right-adjoint twin, the pullback-hom.

- **[[Def - Module over a Monoidal Model Category]]**
	- A **monoid** $R$ in $\mathcal{C}$ is an object with $\mu : R \otimes R \to R$ and $\eta : I \to R$ satisfying associativity and unit laws — a "ring object". A **(left) module** over $R$ is an object $M$ with an action $R \otimes M \to M$ compatible with $\mu$ and $\eta$. When $\mathcal{C}$ is a monoidal model category satisfying the **monoid axiom**, the category $\mathbf{Mod}_R$ of $R$-modules inherits a model structure (weak equivalences and fibrations created by the forgetful functor to $\mathcal{C}$) — this is the Schwede–Shipley theorem. This is the doorway to homotopical algebra: ring spectra, differential graded algebras, and **$E_\infty$-algebras** are monoids in their respective monoidal model categories.

> [!tip] Unlocked: Closed Symmetric Monoidal Categories as Models of Linear Logic *(from Logic / Type Theory)*
> A closed symmetric monoidal category is the categorical semantics of **multiplicative intuitionistic linear logic**, exactly as a [[Def - Cartesian Closed Category|cartesian closed category]] models simply typed lambda calculus. The tensor $\otimes$ models the multiplicative conjunction $\otimes$ ("times"), the internal hom $[B,C]$ models linear implication $B \multimap C$, and the absence of a diagonal $A \to A \otimes A$ is the categorical content of "no contraction" — resources cannot be duplicated. This is the **Curry-Howard-Lambek** correspondence one level out from the cartesian case.

> [!tip] Unlocked: Ring Spectra and Brave New Algebra *(from Stable Homotopy Theory)*
> A monoid in the monoidal model category of **symmetric spectra** is a **ring spectrum**; a commutative one is an $E_\infty$-ring spectrum. The whole program of "brave new algebra" — doing commutative algebra over the sphere spectrum $\mathbb{S}$ instead of over $\mathbb{Z}$, with topological Hochschild homology, Galois extensions of ring spectra, and the chromatic tower — lives in $\mathbf{Mod}_R$ for ring spectra $R$, and exists because modules over a monoid in a (nice) monoidal model category form a model category.

- **[[Ex - Mod_R is closed monoidal but not cartesian closed]]** (⭐)
	- Show $(\mathbf{Mod}_R, \otimes_R, R)$ is closed monoidal with internal hom $\mathrm{Hom}_R$, but not cartesian closed, since the monoidal product $\otimes_R$ is not the categorical product $\oplus$.

- **[[Ex - The internal hom of chain complexes]]** (⭐⭐)
	- Construct the internal hom $[M, N]$ of complexes with the Koszul-sign differential, verify the tensor-hom adjunction, and show $Z_0[M,N]$ is chain maps and $H_0[M,N]$ chain-homotopy classes.

- **[[Ex - Monoids in chain complexes are differential graded algebras]]** (⭐⭐)
	- Show a monoid in $\mathbf{Ch}(R)$ is a differential graded algebra, deriving the graded Leibniz rule $d(ab) = (da)b + (-1)^{|a|}a(db)$ from the requirement that $\mu$ be a chain map.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 Closed Monoidal Categories and Modules]]

## §2 The Pushout-Product Axiom

- **[[Def - Monoidal Model Category]]**
	- A **monoidal model category** is a closed symmetric monoidal category that is also a model category, such that $\otimes$ and the model structure are compatible via two axioms. The **pushout-product axiom** (SM7): if $f$ and $g$ are cofibrations then their pushout-product $f \mathbin{\square} g$ is a cofibration, which is trivial as soon as either $f$ or $g$ is. The **unit axiom**: for a cofibrant replacement $QI \xrightarrow{\sim} I$ of the unit and any cofibrant $X$, the map $QI \otimes X \to I \otimes X \cong X$ is a weak equivalence (automatic when $I$ is cofibrant). These two are exactly what is needed to make the derived tensor and the homotopy category monoidal.

- **[[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor]]**
	- A **two-variable adjunction** $(\otimes, [-,-]_l, [-,-]_r)$ between model categories yields a **Quillen bifunctor** precisely when its pushout-product satisfies the pushout-product axiom; equivalently when the adjoint **pullback-hom** $\langle i, p\rangle$ is a fibration whenever $i$ is a cofibration and $p$ a fibration (trivial if either is). The pushout-product axiom for $\otimes$ is therefore the same statement as a Quillen-bifunctor condition, and is what packages the tensor and internal hom into a single homotopically coherent adjunction. This is the homotopical lift of "a closed monoidal structure is an adjunction $- \otimes B \dashv [B, -]$".

> [!tip] Unlocked: The Pushout-Product as the Engine of Enriched Homotopy Theory *(from ∞-Category Theory)*
> The pushout-product axiom, stated for a two-variable adjunction $\mathcal{V} \times \mathcal{M} \to \mathcal{M}$ where $\mathcal{V}$ is a monoidal model category, is exactly the axiom for a **$\mathcal{V}$-model category** (an enriched model category). When $\mathcal{V} = \mathbf{sSet}$ this is **SM7** in Quillen's original sense, the definition of a simplicial model category, and the route by which mapping spaces $\mathrm{map}(X, Y)$ become homotopy-invariant and the homotopy theory acquires its ∞-categorical refinement.

- **[[Ex - The pushout-product of boundary inclusions of simplices]]** (⭐⭐)
	- Compute $\partial\Delta^m \mathbin{\square} \partial\Delta^n$ in $\mathbf{sSet}$ as the inclusion of the boundary $\partial(\Delta^m \times \Delta^n)$ of the prism, a monomorphism, verifying the pushout-product axiom on generators.

- **[[Ex - Reducing the pushout-product axiom to generating cofibrations]]** (⭐⭐)
	- Prove the closure lemma: the class $\{f : f \mathbin{\square} g \in \text{cof}\}$ is closed under pushout, transfinite composition, and retract, so the axiom reduces to a check on generators.

- **[[Ex - Transposing the pushout-product to the pullback-hom]]** (⭐⭐⭐)
	- Prove the lifting adjunction $i \mathbin{\square} j \perp p \iff i \perp \langle j, p\rangle$ and deduce the equivalence of the pushout-product and pullback-hom forms of the axiom.

> [!note] Exercise Index — §2
> [[Exercise Index - §2 The Pushout-Product Axiom]]

## §3 The Homotopy Category of a Monoidal Model Category

- **[[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal]]**
	- If $\mathcal{C}$ is a monoidal model category, then $\mathrm{Ho}(\mathcal{C})$ is a closed symmetric monoidal category under the **derived tensor product** $A \otimes^{\mathbf{L}} B = QA \otimes QB$, with unit $QI$ and a derived internal hom. The total derived functors of $\otimes$ and $[-, -]$ supply the structure, and the coherence isomorphisms descend from $\mathcal{C}$. Concretely: in $\mathbf{Ch}(R)$ the derived tensor computes Tor, $H_n(M \otimes^{\mathbf{L}}_R N) = \mathrm{Tor}^R_n(M, N)$; in $\mathbf{sSet}$ and $\mathbf{Top}$ the derived tensor is the (homotopy) product; in symmetric spectra it is the smash product on the **stable homotopy category**.

- **[[Ex - The derived tensor on chain complexes computes Tor]]** (⭐⭐)
	- Show that for $R$-modules $M, N$ regarded as complexes in degree zero, $\mathrm{Ho}(\mathbf{Ch}(R))(M, N[n])$ and the derived tensor recover $\mathrm{Tor}^R_n(M, N) = H_n(M \otimes^{\mathbf{L}}_R N)$, by computing with a projective resolution.

- **[[Ex - The unit of the derived tensor and non-cofibrant units]]** (⭐⭐)
	- Show $QI$ is the unit for $\otimes^{\mathbf{L}}$, that the unit axiom is automatic when $I$ is cofibrant, and that it is non-vacuous for symmetric spectra where the sphere $\mathbb{S}$ is not cofibrant.

- **[[Ex - The derived tensor is well-defined independent of replacement]]** (⭐⭐)
	- Prove $A \otimes^{\mathbf{L}} B = QA \otimes QB$ is independent of the chosen cofibrant replacements and functorial on $\mathrm{Ho}(\mathcal{C})$, localizing where the pushout-product axiom is used.

> [!tip] Unlocked: Symmetric Monoidal Structure on a Triangulated Category *(from Stable Homotopy / Derived Algebra)*
> When $\mathcal{C}$ is in addition a stable model category, $\mathrm{Ho}(\mathcal{C})$ is a **triangulated category** that is *also* symmetric monoidal, and the two structures are compatible (the tensor is exact in each variable). This is the structure of the **derived category** $D(R)$ with $\otimes^{\mathbf{L}}$ and of the **stable homotopy category** with $\wedge$ — the natural home of the universal coefficient and Künneth spectral sequences, and the starting point for tensor-triangular geometry.

> [!note] Exercise Index — §3
> [[Exercise Index - §3 The Homotopy Category of a Monoidal Model Category]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The questions in this chapter cluster around five recurring goals. The first and most basic is to **verify the pushout-product axiom** for a candidate monoidal model category: given $\otimes$ and a model structure, check that cofibration-$\square$-cofibration is a cofibration and that triviality propagates. Because cofibrations in the standard examples are generated by a set $I$ of maps (the category is cofibrantly generated), this reduces to a *finite* check on generators — the second recurring target, **reducing an axiom to generators**, via the fact that pushout-products of generating cofibrations generate the cofibrations of the product. A third target is to **compute a derived tensor or internal hom**: identify $A \otimes^{\mathbf{L}} B$ with a known invariant (Tor, the smash product, the homotopy product) by cofibrantly replacing and computing. A fourth is to **establish that two monoidal model categories are monoidally Quillen equivalent**, so that their homotopy categories agree *as symmetric monoidal categories* — this is what makes "the" stable homotopy category well-defined despite many competing point-set models. The fifth is to **build a model structure on modules or algebras**, i.e. transfer the model structure along the free-forgetful adjunction, which needs the monoid axiom. These five — verify SM7, reduce to generators, compute a derived functor, prove a monoidal equivalence, lift to modules — are the targets, and they recur because each is a way of certifying that an algebraic operation has been made homotopy-invariant.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **The category is cofibrantly generated**, with explicit generating (trivial) cofibrations $I$ and $J$ — the richest source, because it turns every "for all cofibrations" axiom into a check on the generators and lets the small object argument build factorizations. **One factor is cofibrant**, which is the hypothesis under which tensoring preserves weak equivalences (by Ken Brown's lemma applied to $- \otimes (\text{cofibrant})$) — this is the workhorse that makes $\otimes^{\mathbf{L}}$ well-defined. **The unit is cofibrant**, a frequent simplification that makes the unit axiom automatic and removes the need to track $QI$ versus $I$. **The monoidal structure is symmetric**, which collapses the two internal homs into one and makes the smash-product / tensor commutative on the homotopy category. **An explicit adjunction $- \otimes B \dashv [B, -]$ is in hand**, so that a pushout-product condition can be transposed into a pullback-hom condition and checked on whichever side is convenient. The recurring move is to route a source to a target: cofibrant generation routes through the pushout-product-of-generators lemma to SM7; a cofibrant factor routes through Ken Brown to homotopy-invariance of $\otimes$; an adjunction routes through transposition to the equivalent fibration condition. The [[Model Categories — Monoidal Model Categories#Problem-Solving Strategy|Problem-Solving Strategy]] makes these routes explicit.

---

# Legal Operations

These are the moves nearly every problem in this chapter is assembled from. When stuck, scan the list and try each. Everything here is self-contained.

**Legal operations:**

1. **Form the pushout-product of two maps.** Given $f : U \to V$ and $g : X \to Y$, build the pushout $P = (V \otimes X) \sqcup_{U \otimes X} (U \otimes Y)$ of $V \otimes X \leftarrow U \otimes X \rightarrow U \otimes Y$ (a [[Def - Pullback and Pushout|pushout]] in $\mathcal{C}$), and take the induced map $f \mathbin{\square} g : P \to V \otimes Y$. This is the canonical way to combine two morphisms multiplicatively while remembering their "boundaries". *Trigger:* you must check a compatibility of $\otimes$ with cofibrations, or you see two maps you want to tensor "relatively". *Pattern:* "the pushout-product of cofibrations is a cofibration, trivial if either is".

2. **Transpose a pushout-product condition into a pullback-hom condition.** Because $- \otimes B \dashv [B, -]$ in a [[Def - Closed Monoidal Category|closed monoidal category]], a lifting problem for $f \mathbin{\square} g$ against a map $p$ transposes to a lifting problem for $f$ (or $g$) against the **pullback-hom** $\langle g, p\rangle : [Y, Z] \to [X, Z] \times_{[X, W]} [Y, W]$. Use whichever side is easier to verify. *Trigger:* "the pushout-product axiom is awkward on the tensor side"; transpose and check the internal hom is a fibration.

3. **Reduce an axiom to the generating (trivial) cofibrations.** In a cofibrantly generated category, cofibrations are the retracts of transfinite cellular extensions of the generators $I$. The class $\{f : f \mathbin{\square} g \text{ is a cofibration for all cofibrations } g\}$ is closed under pushout, transfinite composition, and retract, so it suffices to verify the pushout-product axiom on $I \mathbin{\square} I$ and $I \mathbin{\square} J$. *Trigger:* an axiom quantified over all cofibrations; replace "all" by "generators".

4. **Cofibrantly replace before tensoring (form the derived tensor).** $\otimes$ does not preserve weak equivalences in general, but $- \otimes Z$ does when $Z$ is cofibrant. So define $A \otimes^{\mathbf{L}} B = QA \otimes QB$ using [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]] $Q$. *Trigger:* a tensor appears on a homotopy category, or you want a homotopy-invariant product. *Pattern:* "replace, then tensor; never tensor naively in $\mathrm{Ho}$".

5. **Invoke Ken Brown's lemma to get homotopy-invariance from the cofibrant case.** A functor that sends trivial cofibrations between cofibrant objects to weak equivalences preserves *all* weak equivalences between cofibrant objects. Applied to $- \otimes Z$ (for cofibrant $Z$), the pushout-product axiom's triviality clause is exactly the trivial-cofibration hypothesis, so $- \otimes Z$ is homotopical on cofibrant objects. *Trigger:* you have an axiom on trivial cofibrations and want a statement about all weak equivalences.

6. **Use the unit axiom to compare $QI \otimes X$ with $X$.** When the unit $I$ is not cofibrant, $QI \otimes X$ replaces $I \otimes X \cong X$; the unit axiom says this comparison is a weak equivalence for cofibrant $X$, so $QI$ is a genuine unit on $\mathrm{Ho}(\mathcal{C})$. *Trigger:* the unit object is not cofibrant (as for symmetric spectra), and you need the unit laws to descend.

7. **Transfer a model structure along a free-forgetful adjunction.** To put a model structure on $\mathbf{Mod}_R$ or on algebras, declare weak equivalences and fibrations to be those of $\mathcal{C}$ under the forgetful functor, and use the monoid axiom plus the small object argument to build the cofibrant factorizations. *Trigger:* "do homotopy theory in modules/algebras over a monoid". *Pattern:* "create $\mathcal{W}$ and fibrations from the underlying category; generate cofibrations freely".

8. **Pass to the homotopy category and use the derived adjunction.** A monoidal Quillen adjunction descends to a (lax) monoidal adjunction on homotopy categories via [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]]. Use this to identify a derived tensor with a known operation, or to prove two homotopy categories agree monoidally. *Trigger:* comparing two models, or transporting a computation along an equivalence.

9. **Build the internal hom on $\mathrm{Ho}$ by fibrant-and-cofibrant replacement.** The derived internal hom is $\mathbf{R}[-, -] = [Q(-), R(-)]$: cofibrantly replace the source, fibrantly replace the target. *Trigger:* you need a homotopy-invariant mapping object, e.g. a derived $\mathrm{Hom}$ computing Ext.

**Illegal but tempting operations:**

> [!warning] 1. Tensoring on the homotopy category with the *naive* $\otimes$
> It is tempting to define $A \otimes B$ on $\mathrm{Ho}(\mathcal{C})$ by just tensoring representatives. But $\otimes$ does not preserve weak equivalences, so this is not well-defined: in $\mathbf{Ch}(\mathbb{Z})$, $\mathbb{Z}/2 \simeq [\mathbb{Z} \xrightarrow{2} \mathbb{Z}]$, yet $\mathbb{Z}/2 \otimes \mathbb{Z}/2$ has homology only in degree $0$ while $[\mathbb{Z} \xrightarrow{2}\mathbb{Z}] \otimes \mathbb{Z}/2$ has homology in degrees $0$ and $1$ — the latter being $\mathrm{Tor}^{\mathbb{Z}}_1(\mathbb{Z}/2,\mathbb{Z}/2)$. The operation becomes legal exactly when you replace one factor by a cofibrant object first: $\otimes^{\mathbf{L}}$.

> [!warning] 2. Assuming the pushout-product of two cofibrations is just the tensor of the cofibrations
> One might guess $f \mathbin{\square} g$ is $f \otimes g : U \otimes X \to V \otimes Y$. It is not: $f \otimes g$ forgets the relative structure, and its source is $U \otimes X$, not the pushout $P$. The map $f \otimes g$ factors as $V \otimes Y \leftarrow P \xleftarrow{} U \otimes X$, with $f \mathbin{\square} g$ the genuinely informative piece. Using $f \otimes g$ in place of $f \mathbin{\square} g$ gives a *false* axiom — $f \otimes g$ of two cofibrations need not be a cofibration. The pushout corner $P$ is exactly what repairs this.

> [!warning] 3. Treating the unit $I$ as automatically cofibrant
> In many examples ($\mathbf{Ch}(R)$ with $R$ cofibrant, $\mathbf{sSet}$ with $\Delta^0$) the unit *is* cofibrant, so one is tempted to drop the unit axiom. But for **symmetric spectra** the sphere spectrum $\mathbb{S}$ (the unit) is *not* cofibrant, and skipping the unit axiom would let $QI \otimes X$ fail to be weakly equivalent to $X$, so $QI$ would not act as a unit on $\mathrm{Ho}$. The operation "ignore the unit axiom" becomes legal exactly when $I$ is cofibrant; otherwise you must verify it.

> [!warning] 4. Assuming modules over any monoid form a model category
> Given a monoid $R$ in a monoidal model category, it is tempting to declare $\mathbf{Mod}_R$ a model category by lifting weak equivalences and fibrations. This can fail: the transferred factorizations need not exist without control over how free modules behave under transfinite composition. The standard counterexample-shaped obstruction is the failure of the **monoid axiom**; Schwede–Shipley isolate it as the exact extra hypothesis that makes the transfer go through. The operation becomes legal precisely when $\mathcal{C}$ satisfies the monoid axiom (and is cofibrantly generated).

---

# Problem-Solving Strategy

The problems in this chapter are won at the moment you decide *which* of the two compatibility axioms is at issue and *which side of the adjunction* you intend to check it on. Almost every exercise is one of five types, and each has a characteristic source pattern and route.

If the problem **asks you to verify that a given $(\mathcal{C}, \otimes)$ is a monoidal model category**, you are checking the pushout-product axiom and the unit axiom, and the route runs through cofibrant generation. The single most important reduction is that the pushout-product of cofibrations is a cofibration *if and only if* the pushout-products of the generating cofibrations are, and likewise for the trivial case. So factor the problem: identify the generating (trivial) cofibrations $I$, $J$; compute the pushout-products $I \mathbin{\square} I$ and $I \mathbin{\square} J$ on generators; recognize them as (trivial) cofibrations. For $\mathbf{sSet}$ the generators are boundary inclusions $\partial\Delta^n \hookrightarrow \Delta^n$ and their pushout-products are again monomorphisms (every monomorphism is a cofibration); for $\mathbf{Ch}(R)$ the generators are sphere-into-disk maps $S^{n-1} \to D^n$ and their pushout-products are again degreewise-split monos with projective cokernel. The unit axiom is then a one-line check or automatic.

If the problem **asks you to compute a derived tensor or internal hom**, the assumption pattern is that you can cofibrantly (or fibrantly) replace explicitly, and the route is "replace, then compute on the point set". Do not work in $\mathrm{Ho}$ abstractly; descend to $\mathcal{C}$, cofibrantly replace one factor — in $\mathbf{Ch}(R)$ this is a projective resolution — tensor there, and read off the homology. The non-obvious discipline is to remember that you need replace only *one* factor when the other is already cofibrant, and that the answer is independent of the choice by [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the bifunctor theorem]]. The signature outcome is Tor and Ext: $H_*(M \otimes^{\mathbf{L}} N) = \mathrm{Tor}_*(M, N)$ and $H^*\mathbf{R}[M, N] = \mathrm{Ext}^*(M, N)$.

If the problem **asks you to prove the homotopy category is monoidal**, the route is the bifunctor theorem followed by descent. The Quillen-bifunctor property of $(\otimes, [-,-])$ gives total derived functors that preserve the relevant structure, and the coherence isomorphisms — associativity, unit, symmetry — descend from $\mathcal{C}$ because they are weak equivalences between cofibrant objects, hence isomorphisms in $\mathrm{Ho}$. The work is entirely in the bifunctor theorem; the descent of coherence is formal once the derived tensor is known to be well-defined.

If the problem **asks you to lift the structure to modules or algebras**, the assumption you need is the monoid axiom, and the route is transfer along free-forgetful. You declare the weak equivalences and fibrations of $\mathbf{Mod}_R$ to be those detected by the forgetful functor, and you use the small object argument plus the monoid axiom to manufacture the cofibrant factorizations. The decision point is recognizing that the monoid axiom (not merely the pushout-product axiom) is the hypothesis at stake — the pushout-product axiom controls $\mathcal{C}$ itself, the monoid axiom controls what happens when you freely adjoin module structure.

If the problem **asks you to compare two models monoidally**, you are after a monoidal Quillen equivalence, and the route is to exhibit a Quillen adjunction whose left adjoint is (lax or strong) monoidal and whose derived functor is an equivalence, then check the comparison maps for the monoidal structure are weak equivalences on cofibrant objects. This is how one proves that all the competing models of spectra present the *same* symmetric monoidal stable homotopy category.

A meta-strategy threads through all five: **whenever a homotopical statement about $\otimes$ resists, transpose it to a statement about the internal hom $[-,-]$, or restrict it to cofibrant objects, or both.** The pushout-product axiom is precisely the device that makes both moves legitimate — every question in this chapter is the question "has this algebraic operation been made to respect weak equivalences, and on which objects?".

---

# Most Reusable Properties

- **[[Def - Monoidal Model Category|The pushout-product axiom (SM7)]]**: cofibration $\square$ cofibration is a cofibration, trivial if either factor is. This is the most-used single fact in the chapter because it is the *generator* of every homotopical compatibility: it implies $- \otimes Z$ preserves cofibrations and (via Ken Brown) weak equivalences between cofibrant objects, it implies the internal hom $[Z, -]$ preserves fibrations, and it reduces — in a cofibrantly generated category — to a finite check on generators. Reach for it whenever you must move a tensor past a weak equivalence; its disguised use is *negative*, ruling out a putative monoidal model structure by exhibiting two cofibrations whose pushout-product is not a cofibration.

- **[[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|The pushout-product / pullback-hom adjunction]]**: $f \mathbin{\square} g$ lifts against $p$ iff $f$ lifts against $\langle g, p\rangle$. This is the workhorse for *transposition*: any awkward tensor-side condition becomes an internal-hom-side condition and vice versa. The recognizable setup is "I cannot see why this pushout-product is trivial" — transpose to the pullback-hom and check it is a trivial fibration, which is often visibly an RLP. It is also the abstract reason the derived tensor and derived internal hom are *simultaneously* well-defined: they are two faces of one Quillen bifunctor.

- **[[Def - Cofibrant and Fibrant Objects|Cofibrant replacement before tensoring]]**: $A \otimes^{\mathbf{L}} B = QA \otimes QB$. This is more reusable than any specific computation because it is the universal recipe for making *any* non-homotopical functor homotopical: replace by cofibrant, apply, and the answer is independent of the replacement. Its typical use is to convert "$\otimes$ is broken on $\mathrm{Ho}$" into "$\otimes^{\mathbf{L}}$ works", and it specializes to projective resolution in $\mathbf{Ch}(R)$, to CW approximation in $\mathbf{Top}$, and to cofibrant ring-spectrum replacement in spectra.

- **[[Def - Closed Monoidal Category|Closedness — internal hom right adjoint to tensor]]**: $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C])$. Reach for this whenever you want to *internalize* a hom-set as an object, to currying-transpose a two-variable map, or to apply [[Thm - Right Adjoints Preserve Limits|RAPL]] to deduce that $[B, -]$ preserves limits while $- \otimes B$ preserves colimits. In the homotopical setting it is the precondition that even lets the pullback-hom be defined, and hence the precondition for the whole Quillen-bifunctor formalism.

- **[[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|The derived monoidal structure on Ho(𝒞)]]**: $(\mathrm{Ho}(\mathcal{C}), \otimes^{\mathbf{L}}, QI)$ is closed symmetric monoidal. This is the payoff property and is used as a black box downstream: it is what makes the derived category a tensor category, the stable homotopy category a smash-product category, and tensor-triangular geometry possible. Recognize its applicability whenever you have certified the pushout-product and unit axioms and want to *do algebra* in the homotopy category.

---

# Bridges

1. **Homological algebra — the derived tensor product and Tor.** The category $\mathbf{Ch}(R)$ of chain complexes, with its tensor product $\otimes_R$ and quasi-isomorphisms as weak equivalences, is the prototype monoidal model category: cofibrant objects are (roughly) the complexes of projectives, so cofibrant replacement is **projective resolution**. The derived tensor $\otimes^{\mathbf{L}}_R$ is then literally "resolve and tensor", and its homology is the classical derived functor $\mathrm{Tor}^R_n(M, N) = H_n(M \otimes^{\mathbf{L}}_R N)$. The pushout-product axiom for $\mathbf{Ch}(R)$ is the homotopical content of the fact that tensoring with a complex of projectives is exact, and the whole apparatus of derived functors — **Tor**, **Ext**, the universal coefficient and Künneth theorems — is the $\mathbf{Ch}(R)$ shadow of this chapter's general machinery. See [[Def - Tensor Product of Modules]] and [[Thm - Universal Property of the Tensor Product of Modules]].

2. **Stable homotopy theory — the smash product and ring spectra.** The category of **symmetric spectra** (or orthogonal spectra, or $S$-modules) is a monoidal model category whose tensor is the smash product $\wedge$ and whose unit is the sphere spectrum $\mathbb{S}$. Its homotopy category is the **stable homotopy category**, and the derived smash product makes it symmetric monoidal — the structure underlying all of stable homotopy theory. Crucially $\mathbb{S}$ is *not* cofibrant, which is exactly why the unit axiom is part of the definition rather than a triviality. Monoids here are **ring spectra**, commutative monoids are $E_\infty$-rings, and modules over them (this chapter's [[Def - Module over a Monoidal Model Category|modules]]) are where "brave new algebra" happens.

3. **Algebraic geometry — the derived category of coherent sheaves.** On a scheme $X$, the category of complexes of $\mathcal{O}_X$-modules carries a tensor product $\otimes_{\mathcal{O}_X}$ and quasi-isomorphisms; its homotopy/derived category $D(X)$ is symmetric monoidal under the derived tensor $\otimes^{\mathbf{L}}_{\mathcal{O}_X}$, with unit the structure sheaf $\mathcal{O}_X$. (A **scheme** here is a space locally modeled on the prime spectrum $\mathrm{Spec}\,R$ of a commutative ring — the geometric object whose ring of functions is $R$; **coherent sheaves** are the geometric analogue of finitely generated modules.) The derived tensor on $D(X)$ is the precise sense in which "tensoring sheaves" is made homotopy-invariant, and the Fourier–Mukai transforms and tensor-triangular geometry of modern algebraic geometry are built on this monoidal structure being well-defined — a direct instance of this chapter's theorem.

4. **Logic and type theory — closed symmetric monoidal categories as models of linear logic.** Just as a [[Def - Cartesian Closed Category|cartesian closed category]] is the categorical model of simply typed lambda calculus and intuitionistic logic (the Curry-Howard-Lambek correspondence), a [[Def - Closed Monoidal Category|closed symmetric monoidal category]] is the model of *linear* logic: $\otimes$ is the multiplicative conjunction, $[B, C]$ is linear implication $B \multimap C$, and the absence of a diagonal map $A \to A \otimes A$ encodes the linear-logic prohibition on duplicating resources. The internal hom of this chapter is, on the nose, the implication connective of a substructural logic, and the homotopical refinement (a monoidal model category) is what a *homotopy-coherent* such model would present.

---

# Insights

**The unifying frame: a monoidal model category is a tensor product that has learned to respect homotopy.** Everything in this chapter is one idea seen from different angles. A monoidal category gives you $\otimes$; a model category gives you a notion of "same up to homotopy"; the trouble is that $\otimes$ ignores homotopy — it can take weakly equivalent inputs to inequivalent outputs. The pushout-product axiom is the precise discipline that teaches $\otimes$ to respect homotopy, *but only on cofibrant objects*, and the derived tensor is the universal way to use that restricted good behaviour on all objects, by replacing first. Tor is the name of the error you make if you forget to replace. Once you see the chapter this way, the unit axiom, the Quillen-bifunctor packaging, the descent to $\mathrm{Ho}$, and the lift to modules are all the same demand applied to successively richer structure: make the algebra homotopy-invariant.

**The true name of the pushout-product is "relative tensor".** The formula $f \mathbin{\square} g : (V \otimes X) \sqcup_{U \otimes X} (U \otimes Y) \to V \otimes Y$ looks like a piece of diagram-chasing machinery, but its meaning is geometric: if $f$ and $g$ are inclusions of "cells", then $f \mathbin{\square} g$ is the inclusion of the product cell *relative to its boundary*. The pushout corner $P$ is exactly the boundary $\partial(V \otimes Y)$ built from the two faces $V \otimes X$ and $U \otimes Y$ glued along the corner $U \otimes X$, and $f \mathbin{\square} g$ attaches the interior. This is why $\square$ of cofibrations is a cofibration: products of cells are cells, attached along their boundaries. When you see $\square$, picture $\partial(\text{box}) \hookrightarrow \text{box}$, the boundary-relative product. This picture is also the reason $\partial\Delta^m \mathbin{\square} \partial\Delta^n$ relates to $\partial\Delta^{m+n}$, the combinatorial heart of why $\mathbf{sSet}$ is monoidal.

**Closedness is what lets you check the axiom on whichever side is easier.** The pushout-product axiom is a statement about cofibrations and the tensor; its adjoint, the pullback-hom condition, is a statement about fibrations and the internal hom. They are *literally the same condition*, related by the adjunction transpose, because a lifting problem for $f \mathbin{\square} g$ against $p$ is the same data as a lifting problem for $f$ against $\langle g, p\rangle$. This is more than a convenience: it is the reason the derived tensor and the derived internal hom are well-defined *simultaneously*, as the two adjoint halves of a single Quillen bifunctor. The trigger-reaction pattern is sharp — whenever a pushout-product is hard to analyze, transpose it; the internal hom often wears its fibration property on its sleeve as a visible right lifting property.

**The unit object is the subtle corner, and symmetric spectra are why.** It is natural to assume the unit $I$ behaves like the cofibrant objects, since in chain complexes and simplicial sets it does. But the unit is special: it is forced on you by the monoidal structure, not chosen, and there is no reason it should be cofibrant. The discovery — central to the modern foundations of stable homotopy theory — is that the sphere spectrum $\mathbb{S}$, the unit for the smash product, is *not* cofibrant in any of the standard symmetric monoidal models of spectra. This is not a defect to be engineered away; it is intrinsic, and the unit axiom is the honest accounting for it. The axiom says: even though $I$ is not cofibrant, its cofibrant replacement $QI$ still acts as a unit after deriving. The lesson generalizes — when an algebraic structure has a distinguished element you did not choose, check separately that it survives homotopy, because the cofibrant objects you *did* build will not vouch for it.

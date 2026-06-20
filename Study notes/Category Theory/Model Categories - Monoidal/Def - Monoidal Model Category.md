---
type: definition
subject: model-categories
prereqs:
  - "Def - Closed Monoidal Category"
  - "Def - Model Category"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a category that is both a [[Def - Closed Monoidal Category|closed symmetric monoidal category]] $(\mathcal{C}, \otimes, I)$ and a [[Def - Model Category|model category]] (weak equivalences $\mathcal{W}$, cofibrations $\rightarrowtail$, fibrations $\twoheadrightarrow$). A **trivial cofibration** is a map that is both a cofibration and a weak equivalence; a **trivial fibration** is both a fibration and a weak equivalence. For maps $f : U \to V$ and $g : X \to Y$, the **pushout-product** is
$$f \mathbin{\square} g : (V \otimes X) \sqcup_{U \otimes X} (U \otimes Y) \longrightarrow V \otimes Y,$$
the map out of the [[Def - Pullback and Pushout|pushout]] $P = (V \otimes X) \sqcup_{U \otimes X} (U \otimes Y)$ induced by $f \otimes 1_Y$ and $1_V \otimes g$. We write $Q$ for [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]], so $QI \xrightarrow{\sim} I$ is a cofibrant replacement of the unit. The full symbol registry is on [[Model Categories — Monoidal Model Categories]].

---

# Axiom Motivation

The motivation is to make the tensor product homotopy-invariant, and the discovery is that one clean axiom does the whole job. We have a category $\mathcal{C}$ carrying both a tensor $\otimes$ and a model structure, and the problem is that they do not automatically cooperate: $\otimes$ need not send weak equivalences to weak equivalences, so it does not descend to $\mathrm{Ho}(\mathcal{C})$. The running witness is $\mathbf{Ch}(\mathbb{Z})$: replacing $\mathbb{Z}/2$ by its quasi-isomorphic projective resolution $[\mathbb{Z} \xrightarrow{2} \mathbb{Z}]$ changes the tensor product up to quasi-isomorphism, and the discrepancy is $\mathrm{Tor}^{\mathbb{Z}}_1(\mathbb{Z}/2, \mathbb{Z}/2)$. So we want exactly the hypothesis that repairs this.

The first instinct — "demand that $\otimes$ preserve weak equivalences" — is both too strong and the wrong shape. Too strong, because almost no useful tensor does (the $\mathbf{Ch}(\mathbb{Z})$ example shows even $\otimes_{\mathbb{Z}}$ fails); wrong shape, because what we actually need is for $\otimes$ to behave on *cofibrant* objects, where homotopy theory is well-controlled, not on all objects. By Ken Brown's lemma, a functor that sends *trivial cofibrations between cofibrant objects* to weak equivalences automatically preserves *all* weak equivalences between cofibrant objects. So the right hypothesis is a statement about how $\otimes$ treats (trivial) cofibrations — and the cleanest such statement that controls both variables at once is the **pushout-product axiom**.

Why the pushout-*product* and not just $f \otimes g$? Consider two cofibrations $f : U \rightarrowtail V$ and $g : X \rightarrowtail Y$. The naive guess that $f \otimes g : U \otimes X \to V \otimes Y$ should be a cofibration is *false*: think of cells, $f = (\partial\Delta^m \hookrightarrow \Delta^m)$ and $g = (\partial\Delta^n \hookrightarrow \Delta^n)$. The product $\Delta^m \times \Delta^n$ is a cell, and the cofibration we want is the inclusion of its *boundary*, $\partial(\Delta^m \times \Delta^n) \hookrightarrow \Delta^m \times \Delta^n$. That boundary is built from the two faces $\Delta^m \times \partial\Delta^n$ and $\partial\Delta^m \times \Delta^n$, glued along their common corner $\partial\Delta^m \times \partial\Delta^n$ — which is exactly the [[Def - Pullback and Pushout|pushout]] $P = (V \otimes X) \sqcup_{U \otimes X} (U \otimes Y)$. The pushout-product $f \mathbin{\square} g : P \to V \otimes Y$ is the boundary-relative inclusion, and *that* is what is a cofibration. The corner $P$ is precisely what corrects the false naive statement; without it the axiom would be wrong.

Now the triviality clause. We want $- \otimes Z$ to be homotopical for cofibrant $Z$, and Ken Brown reduces this to: $- \otimes Z$ sends trivial cofibrations to weak equivalences. Take $g = (\varnothing \to Z)$, the generating datum of "$Z$ is cofibrant", and $f$ a trivial cofibration; then $f \mathbin{\square} g$ degenerates to $f \otimes Z$, and the axiom's demand "$f \mathbin{\square} g$ is trivial whenever $f$ is" says exactly that $f \otimes Z$ is a weak equivalence. So the clause "**$f \mathbin{\square} g$ is a trivial cofibration as soon as either $f$ or $g$ is**" is not an extra decoration; it is the precise content of "tensoring with a cofibrant object preserves trivial cofibrations", which by Ken Brown is "tensoring with a cofibrant object is homotopical". Drop the triviality clause and the derived tensor is not well-defined: tensoring weakly equivalent cofibrant objects could give inequivalent results.

What does the **unit axiom** fix, and why is it separate? The pushout-product axiom controls $\otimes$ but says nothing about the unit object $I$ unless $I$ happens to be cofibrant. If $I$ is cofibrant, the unit laws descend to $\mathrm{Ho}(\mathcal{C})$ automatically: $I \otimes X \cong X$ for cofibrant $X$ and everything is fine. But the unit is forced on you by the monoidal structure, not chosen, and there is no reason it should be cofibrant. The decisive example is **symmetric spectra**, where the sphere spectrum $\mathbb{S}$ — the unit for the smash product — is *not* cofibrant. In that case the derived tensor's unit must be $QI$, and we need to know that $QI$ really acts as a unit: that $QI \otimes X \to I \otimes X \cong X$ is a weak equivalence for cofibrant $X$. That is exactly the **unit axiom**. Drop it and $QI$ might fail to be a unit on $\mathrm{Ho}(\mathcal{C})$, so the derived tensor would have no unit object — a monoidal structure missing its unit is not a monoidal structure. The unit axiom is automatic when $I$ is cofibrant, which is why it is invisible in $\mathbf{Ch}(R)$ (for $R$ a field or otherwise nice) and in $\mathbf{sSet}$, and indispensable for spectra.

A final design point: why insist on *closedness*? Because the pushout-product axiom has an adjoint form, the pullback-hom condition, and the two together are what make the tensor and internal hom into a single Quillen bifunctor (see [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor]]). Closedness is what supplies the internal hom $[-,-]$ to transpose against; without it you could state the pushout-product axiom but lose the right-adjoint half that produces the derived internal hom.

---

# The Definition

A **monoidal model category** is a category $\mathcal{C}$ equipped with
- a [[Def - Closed Monoidal Category|closed symmetric monoidal structure]] $(\otimes, I, [-,-])$, and
- a [[Def - Model Category|model structure]] $(\mathcal{W}, \text{cof}, \text{fib})$,

such that the following two axioms hold.

> **(Pushout-Product Axiom, "SM7").** For cofibrations $f : U \rightarrowtail V$ and $g : X \rightarrowtail Y$, the pushout-product
> $$f \mathbin{\square} g : (V \otimes X) \sqcup_{U \otimes X} (U \otimes Y) \longrightarrow V \otimes Y$$
> is a cofibration. Moreover, if in addition either $f$ or $g$ is a weak equivalence (a trivial cofibration), then $f \mathbin{\square} g$ is a trivial cofibration.

> **(Unit Axiom).** Let $QI \xrightarrow{\ \sim\ } I$ be a cofibrant replacement of the unit. Then for every cofibrant object $X$, the composite
> $$QI \otimes X \longrightarrow I \otimes X \xrightarrow{\ \cong\ } X$$
> (the cofibrant-replacement map of the unit tensored with $X$, followed by the unitor) is a weak equivalence.

When the unit $I$ is itself cofibrant, the unit axiom holds automatically (take $QI = I$), and a monoidal model category with cofibrant unit is the most common situation. The pushout-product axiom is often stated equivalently — via the [[Def - Closed Monoidal Category|tensor-hom adjunction]] — as the **pullback-hom (SM7) condition** on the internal hom: for a cofibration $i$ and a fibration $p$, the pullback-hom $\langle i, p\rangle$ is a fibration, trivial if either $i$ or $p$ is. The two forms are equivalent by transposition, which is the content of [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor]].

---

# Categorical / Structural Definition

Structurally, a monoidal model category is the data making $(\otimes, [-,-])$ a **Quillen two-variable adjunction** (a Quillen bifunctor), together with a homotopical compatibility of the unit. A two-variable adjunction here is the triple $(\otimes, [-,-]_{\ell}, [-,-]_r)$ with natural isomorphisms
$$\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C]_r) \cong \mathcal{C}(B, [A, C]_{\ell}),$$
which in the symmetric case collapses to one internal hom. The pushout-product axiom is exactly the assertion that this two-variable adjunction is a **Quillen bifunctor**: its pushout-product preserves cofibrations and the triviality propagates. The unit axiom is the extra clause ensuring that the cofibrant replacement of the unit $I$ acts as a homotopy unit. In one line: **a monoidal model category is a closed symmetric monoidal category whose tensor/internal-hom adjunction is a Quillen bifunctor and whose unit is homotopically well-behaved.**

From the (∞,1)-categorical viewpoint, a monoidal model category is a *presentation* of a **symmetric monoidal ∞-category**: the underlying ∞-category is $\mathcal{C}[\mathcal{W}^{-1}]$ (as in [[Def - Model Category]]), and the derived tensor $\otimes^{\mathbf{L}}$ presents the ∞-categorical symmetric monoidal product. The model structure is the computable, point-set scaffolding; the intrinsic object it presents is the symmetric monoidal ∞-category, and the two axioms are exactly what guarantees the scaffolding is faithful.

---

# Relate to Other Fields / Compression

A monoidal model category is the homotopical upgrade of a [[Def - Closed Monoidal Category|closed monoidal category]]: it is "a monoidal category whose tensor has been certified to respect weak equivalences on cofibrant objects." The most familiar tensor products become monoidal model structures in their natural homotopy theories. In homological algebra, $\mathbf{Ch}(R)$ with $\otimes_R$ and quasi-isomorphisms is the prototype; the pushout-product axiom is the homotopical content of "tensoring with a complex of projectives is exact", and the resulting derived tensor computes **Tor**. In stable homotopy theory, symmetric spectra with the smash product and the sphere spectrum as unit is the canonical example with *non-cofibrant* unit, which is precisely why the unit axiom was isolated. In ordinary homotopy theory, $\mathbf{sSet}$ and $\mathbf{Top}$ with the cartesian product are monoidal model categories whose derived tensor is the homotopy product.

**True name:** a monoidal model category is **"a closed monoidal category in which cofibration-$\square$-cofibration is a cofibration (trivial if either factor is), with the unit homotopically fixed up."** The operational reflex: when you must move a tensor past a weak equivalence, you may, *provided* you are on cofibrant objects — and the pushout-product axiom is the licence. When you see "monoidal model category", picture "$\otimes^{\mathbf{L}}$ exists and makes $\mathrm{Ho}(\mathcal{C})$ monoidal".

---

# Examples / Corollaries

**Is an instance — $\mathbf{Ch}(R)$ with $\otimes_R$.** Chain complexes with the projective model structure (weak equivalences = quasi-isomorphisms, cofibrations = monomorphisms with degreewise-projective cokernel) form a monoidal model category under $\otimes_R$, unit $R$ in degree zero. The pushout-product axiom reduces to a check on the generating cofibrations $S^{n-1} \to D^n$ (sphere into disk complexes), whose pushout-products are again degreewise-split monos with projective cokernel. The unit is cofibrant when $R$ is projective over itself (always, as a free module of rank one), so the unit axiom is automatic. The derived tensor computes Tor.

**Is an instance — $\mathbf{sSet}$ with $\times$.** Simplicial sets with the Kan–Quillen model structure (cofibrations = monomorphisms) and the cartesian product form a (cartesian) monoidal model category, unit $\Delta^0$. The pushout-product of two monomorphisms is a monomorphism — this is the combinatorial fact that $\partial\Delta^m \times \Delta^n \cup \Delta^m \times \partial\Delta^n \hookrightarrow \Delta^m \times \Delta^n$ is mono — so the pushout-product axiom holds; $\Delta^0$ is cofibrant (everything is), so the unit axiom is automatic. This cartesian monoidal model structure is what makes $\mathbf{sSet}$ a *simplicial* model category, enriching homotopy theory over itself.

**Is an instance — symmetric spectra with $\wedge$.** The category of symmetric spectra with its stable model structure and the smash product $\wedge$ is a symmetric monoidal model category whose unit is the sphere spectrum $\mathbb{S}$. Crucially $\mathbb{S}$ is **not** cofibrant, so the unit axiom is a genuine, non-vacuous hypothesis here — and it holds. The homotopy category is the **stable homotopy category** with its smash product. This example is the historical reason the unit axiom is part of the definition.

**Is NOT an instance — $\mathbf{Ch}(R)$ with $\otimes_R$ but *all* monos as cofibrations.** If one tried to use a model structure whose cofibrations were *all* monomorphisms (not just those with projective cokernel), the pushout-product axiom would fail: tensoring with a non-projective module can destroy exactness, so $f \mathbin{\square} g$ need not stay a cofibration in the wrong sense. The lesson is that the monoidal model structure is a property of the *whole package* $(\otimes, \mathcal{W}, \text{cof}, \text{fib})$, not of $\otimes$ alone — choosing the cofibrations to be compatible with $\otimes$ is the substance.

**Is NOT an instance — a monoidal category with the trivial model structure and a non-cofibrant-respecting tensor.** Put on $\mathbf{Ch}(\mathbb{Z})$ the *trivial* model structure (weak equivalences = isomorphisms only). Then every object is cofibrant and fibrant, the pushout-product axiom holds vacuously, but the "homotopy category" is just $\mathbf{Ch}(\mathbb{Z})$ itself with the *naive* tensor — and now $\mathbb{Z}/2 \otimes \mathbb{Z}/2$ is computed naively, *not* by Tor. This is not a failure of the axioms; it is a reminder that the derived tensor depends on the weak equivalences, and only the quasi-isomorphism structure produces Tor. The trivial model structure is a monoidal model category, but a useless one for this purpose.

**Calibration check.** Verify that if $I$ is cofibrant then the unit axiom holds (take $QI = I$ and the map is the unitor, an isomorphism). Verify that taking $g = (\varnothing \to Z)$ for cofibrant $Z$ turns "$f \mathbin{\square} g$ is a trivial cofibration when $f$ is trivial" into "$f \otimes Z$ is a weak equivalence when $f$ is a trivial cofibration", recovering homotopy-invariance of $- \otimes Z$. If you can explain *why* the corner pushout $P$ is needed in $f \mathbin{\square} g$ — because $f \otimes g$ alone is not a cofibration, the boundary structure must be remembered — you have understood the axiom.

---

# Unlocked by This

> [!tip] The Derived Tensor Product and a Monoidal Homotopy Category *(from this chapter)*
> The two axioms are exactly what is needed for [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|Ho(𝒞) to be closed symmetric monoidal]] under the derived tensor $\otimes^{\mathbf{L}}$, with unit $QI$. The pushout-product axiom makes $\otimes^{\mathbf{L}}$ well-defined and associative; the unit axiom makes $QI$ a genuine unit.

> [!tip] Model Structures on Modules and Algebras *(from Stable Homotopy / Derived Algebra)*
> Once $\mathcal{C}$ is a monoidal model category satisfying the additional **monoid axiom**, the category of [[Def - Module over a Monoidal Model Category|modules]] over a monoid $R$, and even the category of $R$-algebras, inherits a model structure (Schwede–Shipley). This is the foundation for the homotopy theory of **ring spectra**, **differential graded algebras**, and **$E_\infty$- and $A_\infty$-algebras**.

> [!tip] Symmetric Monoidal ∞-Categories *(from Higher Category Theory)*
> A monoidal model category presents a **symmetric monoidal ∞-category**, the intrinsic object underlying the homotopy theory. The point-set axioms here are the computable scaffolding for the ∞-categorical tensor product that Lurie's *Higher Algebra* takes as primitive; monoidal Quillen equivalences are how one proves two such presentations agree, e.g. that all models of spectra give the same symmetric monoidal stable homotopy category.

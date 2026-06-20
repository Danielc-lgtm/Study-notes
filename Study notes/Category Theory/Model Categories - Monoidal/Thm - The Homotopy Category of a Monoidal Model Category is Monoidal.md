---
type: theorem
subject: model-categories
prereqs:
  - "Def - Monoidal Model Category"
  - "Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor"
  - "Thm - The Homotopy Category of a Model Category"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Closed Monoidal Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $(\mathcal{C}, \otimes, I, [-,-])$ is a [[Def - Monoidal Model Category|monoidal model category]] (closed symmetric monoidal, with the pushout-product and unit axioms). We write $\mathrm{Ho}(\mathcal{C}) = \mathcal{C}[\mathcal{W}^{-1}]$ for the [[Thm - The Homotopy Category of a Model Category|homotopy category]], $Q$ for [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]] ($QX \xrightarrow{\sim} X$) and $R$ for fibrant replacement. The **derived tensor product** is $A \otimes^{\mathbf{L}} B := QA \otimes QB$ and the **derived internal hom** is $\mathbf{R}[A, B] := [QA, RB]$. The unit of the derived structure is $QI$. The full symbol registry is on [[Model Categories — Monoidal Model Categories]].

---

# Statement

> **Theorem (Homotopy Category of a Monoidal Model Category).** Let $\mathcal{C}$ be a [[Def - Monoidal Model Category|monoidal model category]]. Then the homotopy category $\mathrm{Ho}(\mathcal{C})$ is a closed symmetric monoidal category, with:
> - tensor the **derived tensor product** $\otimes^{\mathbf{L}}$, where $A \otimes^{\mathbf{L}} B = QA \otimes QB$;
> - unit object $QI$, the cofibrant replacement of the unit $I$;
> - internal hom the **derived internal hom** $\mathbf{R}[A, B] = [QA, RB]$;
> - associator, unitors, and symmetry obtained as the images in $\mathrm{Ho}(\mathcal{C})$ of those of $\mathcal{C}$.
>
> The localization functor $\gamma : \mathcal{C} \to \mathrm{Ho}(\mathcal{C})$ is **lax monoidal**, and is strong monoidal on cofibrant objects. Moreover the construction is invariant: a **monoidal Quillen equivalence** $\mathcal{C} \to \mathcal{D}$ induces a (strong) symmetric monoidal equivalence $\mathrm{Ho}(\mathcal{C}) \simeq \mathrm{Ho}(\mathcal{D})$.

---

# Motivation

This is the theorem the whole chapter is built to reach: it is the precise sense in which a tensor product *survives the passage to homotopy*. You began with a tensor $\otimes$ on $\mathcal{C}$ that did not descend to $\mathrm{Ho}(\mathcal{C})$ — it failed to respect weak equivalences. The pushout-product and unit axioms were imposed exactly to repair this, and this theorem cashes them in: the derived tensor $\otimes^{\mathbf{L}}$ *does* descend, and equips $\mathrm{Ho}(\mathcal{C})$ with a genuine closed symmetric monoidal structure.

The importance is that it makes a long list of "tensor products on homotopy categories" instances of one statement. The derived tensor on the derived category $D(R)$, the smash product on the **stable homotopy category**, the homotopy product on the homotopy category of spaces — these are not three separate constructions but three instances of "the homotopy category of a monoidal model category is monoidal". And the invariance clause is what makes such structures *well-defined*: there are many point-set models of spectra, all monoidally Quillen equivalent, and this theorem guarantees they present *the same* symmetric monoidal stable homotopy category — so one may speak of "the" smash product without reference to a model.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\mathcal{C}$ is a monoidal model category". The skill is recognizing categories that *are* monoidal model categories, sometimes in disguise, so that the conclusion applies.

The first disguised source is **a cofibrantly generated category in which the pushout-products of generators are (trivial) cofibrations**. By the reduction-to-generators lemma, this finite check upgrades to the full pushout-product axiom, so the category is a monoidal model category (modulo the unit axiom) and the conclusion applies. *Example problem:* given that $\mathbf{Ch}(R)$'s generating cofibrations $S^{n-1} \to D^n$ have pushout-products that are again cofibrations, conclude that $D(R) = \mathrm{Ho}(\mathbf{Ch}(R))$ is symmetric monoidal under $\otimes^{\mathbf{L}}_R$.

The second disguised source is **a category that is monoidally Quillen equivalent to a known monoidal model category**. If $\mathcal{D}$ receives a monoidal Quillen equivalence from a monoidal model category $\mathcal{C}$, then $\mathcal{D}$'s homotopy category inherits the monoidal structure by transport, even if verifying the axioms directly in $\mathcal{D}$ is hard. The bridge is the invariance clause. *Example problem:* deduce that the homotopy category of orthogonal spectra is symmetric monoidal by transporting from symmetric spectra along a known monoidal Quillen equivalence.

The third disguised source is **a stable monoidal model category**, where the conclusion combines with stability. If $\mathcal{C}$ is in addition stable (suspension is invertible on $\mathrm{Ho}$), the derived tensor makes $\mathrm{Ho}(\mathcal{C})$ not just monoidal but *tensor-triangulated*. The bridge is that the derived tensor is exact in each variable, compatible with the triangulation. *Example problem:* show the derived category $D(R)$ is tensor-triangulated, with $\otimes^{\mathbf{L}}_R$ exact and compatible with shifts and triangles.

**Targets (Output Amplification)**

The bare conclusion is "$\mathrm{Ho}(\mathcal{C})$ is closed symmetric monoidal". Combined with other inputs it yields concrete invariants and structural theorems.

Combine the conclusion with **a projective resolution** in $\mathbf{Ch}(R)$. The derived tensor $M \otimes^{\mathbf{L}}_R N$ is computed by resolving and tensoring, and its homology is $\mathrm{Tor}^R_*(M, N)$. The further result $E$ is the entire theory of Tor — its balancing, the universal coefficient and Künneth theorems — realized as homology of the derived monoidal product. This is non-obvious because the abstract monoidal structure says nothing about homology a priori; the resolution is what turns the abstract $\otimes^{\mathbf{L}}$ into a computable graded group.

Combine the conclusion with **the closed structure and fibrant replacement**. The derived internal hom $\mathbf{R}[M, N]$ computes derived mapping objects, and in $\mathbf{Ch}(R)$ its cohomology is $\mathrm{Ext}^*_R(M, N)$. The further result is that Tor and Ext are the two derived halves of one closed monoidal structure, $\mathrm{Ho}(\mathcal{C})(A \otimes^{\mathbf{L}} B, C) \cong \mathrm{Ho}(\mathcal{C})(A, \mathbf{R}[B, C])$ — the adjunction that *is* the balancing isomorphism.

Combine the conclusion with **the invariance clause and a chain of Quillen equivalences**. If several models are connected by monoidal Quillen equivalences, their homotopy categories are *monoidally* equivalent, not just equivalent. The further result is the well-definedness of "the symmetric monoidal stable homotopy category" — a single object independent of the model — which is the foundational fact underlying all of structured ring-spectrum theory. This is non-obvious because Quillen equivalence a priori only gives an equivalence of plain categories; the monoidal refinement requires the comparison maps to respect $\otimes^{\mathbf{L}}$, which the *monoidal* Quillen equivalence supplies.

---

# Why Is It True

The reason is that the derived tensor is "honest" on cofibrant objects, and everything in $\mathrm{Ho}(\mathcal{C})$ can be replaced by a cofibrant representative. The pushout-product axiom (through [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the bifunctor theorem]]) guarantees that tensoring cofibrant objects respects weak equivalences, so $\otimes^{\mathbf{L}}(A, B) = QA \otimes QB$ is well-defined: it does not matter which cofibrant replacement you pick, because any two are weakly equivalent and $\otimes$ of cofibrant objects preserves weak equivalences. That single fact is the whole engine.

Now why does the *structure* descend — associativity, unit, symmetry? Because in $\mathcal{C}$ these are given by isomorphisms (the associator $\alpha$, unitors $\lambda, \rho$, symmetry $\beta$), and isomorphisms are in particular weak equivalences. Between cofibrant objects, a weak equivalence becomes an *isomorphism* in $\mathrm{Ho}(\mathcal{C})$. So $\alpha, \beta$, suitably cofibrantly replaced, descend to coherence isomorphisms in $\mathrm{Ho}(\mathcal{C})$, and the pentagon and hexagon diagrams — which commuted in $\mathcal{C}$ — still commute after applying the localization functor, since $\gamma$ is a functor. The coherence is *inherited*, not re-proved.

> **The derived tensor works because $\otimes$ is homotopical on cofibrant objects, and the coherence works because the localization functor carries the commuting coherence diagrams of $\mathcal{C}$ to commuting diagrams in $\mathrm{Ho}(\mathcal{C})$ — isomorphisms in $\mathcal{C}$ becoming isomorphisms in $\mathrm{Ho}(\mathcal{C})$.**

The one place this naive story needs the *unit* axiom is the unit object. The associativity and symmetry come from the bifunctor theorem alone, but the unit $I$ might not be cofibrant, so $I \otimes A$ is not directly the right thing on $\mathrm{Ho}$. The unit axiom is precisely the guarantee that $QI$ — which *is* cofibrant — still satisfies the unit laws up to weak equivalence: $QI \otimes X \xrightarrow{\sim} X$ for cofibrant $X$. So $QI$ is a unit for $\otimes^{\mathbf{L}}$, and that is the only extra input beyond the bifunctor theorem. The theorem is true because the bifunctor theorem handles multiplication and coherence, and the unit axiom handles the unit.

---

# What Makes This Hard

The conceptually hard point is the **unit**: most people prove the multiplicative coherence cleanly and then trip on the fact that $I$ need not be cofibrant, so $\otimes^{\mathbf{L}}$ has unit $QI$, not $I$, and one must check $QI$ satisfies the unit laws — which is exactly the unit axiom, and is *not* automatic. The technical hard point is the **well-definedness of the coherence isomorphisms across replacements**: the associator on $\mathrm{Ho}$ must be shown independent of choices, which requires tracking that the cofibrant-replacement comparison maps are weak equivalences between cofibrant objects (hence isomorphisms in $\mathrm{Ho}$) and that they intertwine the associators. The common error is to assume the naive tensor's coherence descends without checking that the *replacements* are compatible — it is the naturality of $Q$ and the bifunctor property that make this go through.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use the bifunctor theorem to get a well-defined derived tensor on cofibrant objects; transport the associator and symmetry from $\mathcal{C}$ by replacing cofibrantly and noting weak equivalences between cofibrant objects are $\mathrm{Ho}$-isomorphisms; use the unit axiom to install $QI$ as the unit; observe coherence diagrams descend because $\gamma$ is a functor; finally derive the internal hom by the adjoint half of the bifunctor.

**Subgoal decomposition:**

1. **Well-defined derived tensor.** Show $\otimes^{\mathbf{L}}(A, B) = QA \otimes QB$ is a well-defined bifunctor on $\mathrm{Ho}(\mathcal{C})$.
   - *Hint:* By [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the bifunctor theorem]] and Ken Brown, $\otimes$ preserves weak equivalences between cofibrant objects, so the value is independent of the chosen $Q$.
   - *Why needed:* It is the multiplication; nothing else can be defined without it.

2. **Descend the associator and symmetry.** Show $\alpha, \beta$ induce coherence isomorphisms for $\otimes^{\mathbf{L}}$.
   - *Hint:* $\alpha, \beta$ are isomorphisms in $\mathcal{C}$, hence weak equivalences; between cofibrant objects they become isomorphisms in $\mathrm{Ho}(\mathcal{C})$; apply $\gamma$.
   - *Why needed:* The monoidal structure needs its structural isomorphisms.

3. **Install the unit.** Show $QI$ is a two-sided unit for $\otimes^{\mathbf{L}}$.
   - *Hint:* This is exactly the [[Def - Monoidal Model Category|unit axiom]]: $QI \otimes X \to I \otimes X \cong X$ is a weak equivalence for cofibrant $X$, so $QI \otimes^{\mathbf{L}} X \cong X$ in $\mathrm{Ho}$.
   - *Why needed:* A monoidal structure with no unit is not a monoidal structure; this is the one place the unit axiom (not the pushout-product axiom) is used.

4. **Verify coherence.** Show the pentagon, triangle, and hexagon commute for the descended data.
   - *Hint:* They commute in $\mathcal{C}$; the localization $\gamma$ is a functor and sends commuting diagrams to commuting diagrams; cofibrancy makes the comparison maps isomorphisms.
   - *Why needed:* Coherence is part of the definition of a (symmetric) monoidal category.

5. **Derive the internal hom and the closed structure.** Show $\mathbf{R}[A, B] = [QA, RB]$ is right adjoint to $\otimes^{\mathbf{L}}$ in each variable.
   - *Hint:* The adjoint (pullback-hom) half of the bifunctor theorem, via [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] applied to $- \otimes B \dashv [B, -]$.
   - *Why needed:* It upgrades "monoidal" to "closed monoidal", the full statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: The derived tensor is a well-defined bifunctor on the homotopy category
> **Statement:** The assignment $(A, B) \mapsto QA \otimes QB$ descends to a functor $\otimes^{\mathbf{L}} : \mathrm{Ho}(\mathcal{C}) \times \mathrm{Ho}(\mathcal{C}) \to \mathrm{Ho}(\mathcal{C})$, independent of the cofibrant replacement up to canonical natural isomorphism.
>
> **Hint:** Use that $- \otimes Z$ is a left Quillen functor for cofibrant $Z$ (a consequence of the pushout-product axiom) and Ken Brown's lemma to get preservation of weak equivalences between cofibrant objects.
>
> **Why needed:** It is the existence of the multiplication; the rest of the structure is defined on top of it.
>
> > [!note]- Full proof
> > By Lemma 3 of [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the bifunctor theorem]], for cofibrant $Z$ the functor $- \otimes Z$ preserves weak equivalences between cofibrant objects, and symmetrically $Z \otimes -$. Given a weak equivalence $A \xrightarrow{\sim} A'$ between any objects, $QA \xrightarrow{\sim} QA'$ is a weak equivalence between cofibrant objects (naturality of $Q$), so $QA \otimes QB \xrightarrow{\sim} QA' \otimes QB$ is a weak equivalence; similarly in the second variable. Hence $QA \otimes QB$ sends weak equivalences in each variable to weak equivalences, so by the universal property of localization it descends to a functor on $\mathrm{Ho}(\mathcal{C}) \times \mathrm{Ho}(\mathcal{C})$. Two cofibrant replacements $QA, Q'A$ are weakly equivalent (both weakly equivalent to $A$, and weak equivalences between cofibrant objects), so $QA \otimes QB \cong Q'A \otimes Q'B$ in $\mathrm{Ho}(\mathcal{C})$, giving independence of the choice.

> [!note]- Lemma 2: Coherence isomorphisms descend
> **Statement:** The associator $\alpha$ and the symmetry $\beta$ of $\mathcal{C}$ induce natural isomorphisms $\alpha^{\mathbf{L}}, \beta^{\mathbf{L}}$ for $\otimes^{\mathbf{L}}$ on $\mathrm{Ho}(\mathcal{C})$, and the pentagon, triangle, and hexagon diagrams commute.
>
> **Hint:** Isomorphisms are weak equivalences; weak equivalences between cofibrant objects become isomorphisms in $\mathrm{Ho}(\mathcal{C})$; the localization functor preserves commuting diagrams.
>
> **Why needed:** A symmetric monoidal structure is not just a bifunctor; the coherence isomorphisms and their axioms are essential data.
>
> > [!note]- Full proof
> > For cofibrant $A, B, C$, the associator $\alpha_{A,B,C} : (A \otimes B) \otimes C \to A \otimes (B \otimes C)$ is an isomorphism in $\mathcal{C}$, between objects that are tensors of cofibrant objects, hence cofibrant (the tensor of cofibrant objects is cofibrant, since $\varnothing \to A \otimes B$ is the pushout-product $(\varnothing \to A) \mathbin{\square} (\varnothing \to B)$ of two cofibrations, a cofibration by the axiom). Applying the localization functor $\gamma$, $\alpha_{A,B,C}$ becomes an isomorphism $\alpha^{\mathbf{L}}$ in $\mathrm{Ho}(\mathcal{C})$. Naturality and the pentagon/triangle/hexagon relations hold in $\mathcal{C}$; since $\gamma$ is a functor it carries these commuting diagrams to commuting diagrams in $\mathrm{Ho}(\mathcal{C})$. The same applies to $\beta$. For general (non-cofibrant) objects, define the structure via cofibrant replacement and use Lemma 1's natural isomorphisms to transport, which is consistent because $Q$ is functorial.

> [!note]- Lemma 3: $QI$ is a unit for the derived tensor
> **Statement:** For every object $X$, there are natural isomorphisms $QI \otimes^{\mathbf{L}} X \cong X \cong X \otimes^{\mathbf{L}} QI$ in $\mathrm{Ho}(\mathcal{C})$, satisfying the unit coherence with $\alpha^{\mathbf{L}}$.
>
> **Hint:** This is the [[Def - Monoidal Model Category|unit axiom]]: $QI \otimes Z \to I \otimes Z \cong Z$ is a weak equivalence for cofibrant $Z$.
>
> **Why needed:** Without a unit, $\otimes^{\mathbf{L}}$ is only a "semigroup" structure; the unit axiom is the unique input here beyond the bifunctor theorem.
>
> > [!note]- Full proof
> > By definition $QI \otimes^{\mathbf{L}} X = QI \otimes QX$ (note $QI$ is already cofibrant, so its cofibrant replacement is itself up to weak equivalence). The unit axiom states that for cofibrant $QX$, the map $QI \otimes QX \to I \otimes QX \xrightarrow{\cong} QX$ (the cofibrant-replacement map of the unit tensored with $QX$, then the unitor) is a weak equivalence. Both source and target are cofibrant ($QI \otimes QX$ is a tensor of cofibrant objects, hence cofibrant; $QX$ is cofibrant), so this weak equivalence becomes an isomorphism in $\mathrm{Ho}(\mathcal{C})$, giving $QI \otimes^{\mathbf{L}} X \cong QX \cong X$ in $\mathrm{Ho}(\mathcal{C})$. The right-unit isomorphism is symmetric. The triangle axiom relating the unitors to $\alpha^{\mathbf{L}}$ descends as in Lemma 2.

> [!note]- Lemma 4: The derived internal hom is right adjoint to the derived tensor
> **Statement:** For each $B$, the functor $- \otimes^{\mathbf{L}} B$ has a right adjoint $\mathbf{R}[B, -]$ on $\mathrm{Ho}(\mathcal{C})$, with $\mathrm{Ho}(\mathcal{C})(A \otimes^{\mathbf{L}} B, C) \cong \mathrm{Ho}(\mathcal{C})(A, \mathbf{R}[B, C])$. Hence $\mathrm{Ho}(\mathcal{C})$ is closed.
>
> **Hint:** Apply [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] to the Quillen adjunction $- \otimes B \dashv [B, -]$ for fixed cofibrant $B$, supplied by the pullback-hom side of the bifunctor theorem.
>
> **Why needed:** It upgrades the monoidal structure to a *closed* monoidal structure, the full conclusion.
>
> > [!note]- Full proof
> > Fix a cofibrant $B$. The pullback-hom side of [[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|the bifunctor theorem]] shows $[B, -]$ is a right Quillen functor (it preserves fibrations and trivial fibrations), so $- \otimes B \dashv [B, -]$ is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]]. By [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] it descends to an adjunction $\mathbf{L}(- \otimes B) \dashv \mathbf{R}[B, -]$ on homotopy categories, i.e. $(- \otimes^{\mathbf{L}} B) \dashv \mathbf{R}[B, -]$, with $\mathbf{R}[B, C] = [QB, RC]$. The adjunction isomorphism is the stated one. Letting $B$ vary and using the symmetry to handle both variables yields the closed structure on $\mathrm{Ho}(\mathcal{C})$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{C}$ be a monoidal model category.
>
> **Step 0 — preconditions.** $\mathrm{Ho}(\mathcal{C})$ exists with $\mathrm{Ho}(\mathcal{C})(X, Y) = \pi(QRX, QRY)$ by [[Thm - The Homotopy Category of a Model Category|the fundamental theorem]]; $\mathcal{C}$ is bicomplete and closed, so all tensors, internal homs, and (co)limits used below exist; the pushout-product and unit axioms hold by hypothesis.
>
> **Step 1 — the derived tensor.** By Lemma 1, $\otimes^{\mathbf{L}}(A, B) = QA \otimes QB$ descends to a well-defined bifunctor $\otimes^{\mathbf{L}} : \mathrm{Ho}(\mathcal{C}) \times \mathrm{Ho}(\mathcal{C}) \to \mathrm{Ho}(\mathcal{C})$, independent of cofibrant replacement.
>
> **Step 2 — associativity and symmetry.** By Lemma 2, the associator and symmetry of $\mathcal{C}$ descend to natural isomorphisms $\alpha^{\mathbf{L}}, \beta^{\mathbf{L}}$ for $\otimes^{\mathbf{L}}$, with the pentagon and hexagon diagrams commuting (carried over by the localization functor $\gamma$).
>
> **Step 3 — the unit.** By Lemma 3, $QI$ is a two-sided unit for $\otimes^{\mathbf{L}}$, via the unit axiom, with the triangle axiom holding. Thus $(\mathrm{Ho}(\mathcal{C}), \otimes^{\mathbf{L}}, QI, \alpha^{\mathbf{L}}, \lambda^{\mathbf{L}}, \rho^{\mathbf{L}}, \beta^{\mathbf{L}})$ is a symmetric monoidal category.
>
> **Step 4 — closedness.** By Lemma 4, $- \otimes^{\mathbf{L}} B$ has right adjoint $\mathbf{R}[B, -] = [QB, R(-)]$, with $\mathrm{Ho}(\mathcal{C})(A \otimes^{\mathbf{L}} B, C) \cong \mathrm{Ho}(\mathcal{C})(A, \mathbf{R}[B, C])$. So $\mathrm{Ho}(\mathcal{C})$ is closed symmetric monoidal.
>
> **Step 5 — laxness of $\gamma$ and invariance.** The structure maps $\gamma(A) \otimes^{\mathbf{L}} \gamma(B) = QA \otimes QB \to A \otimes B = \gamma(A \otimes B)$ (from $QA \to A$, $QB \to B$) make $\gamma$ lax monoidal; on cofibrant objects these maps are isomorphisms in $\mathrm{Ho}(\mathcal{C})$, so $\gamma$ is strong monoidal there. For invariance: a monoidal Quillen equivalence $F \dashv U$ has $\mathbf{L}F$ strong monoidal (its lax structure maps are weak equivalences between cofibrant objects, hence isomorphisms in $\mathrm{Ho}$) and an equivalence by [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]]; a strong monoidal equivalence is a symmetric monoidal equivalence, so $\mathrm{Ho}(\mathcal{C}) \simeq \mathrm{Ho}(\mathcal{D})$ as symmetric monoidal categories. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Chain complexes — the derived tensor is Tor.** Take $\mathcal{C} = \mathbf{Ch}(R)$. For $R$-modules $M, N$ in degree zero, cofibrantly replace $M$ by a projective resolution $P_\bullet \xrightarrow{\sim} M$; then $M \otimes^{\mathbf{L}}_R N = P_\bullet \otimes_R N$, whose homology is $\mathrm{Tor}^R_*(M, N)$. The monoidal structure on $D(R)$ from this theorem *is* the structure under which Tor is computed. The non-obvious application is that the abstract symmetric monoidal coherence of $D(R)$ specializes to the *balancing* of Tor (it may be computed by resolving either variable).

**Spectra — the smash product and the well-definedness of "the" stable homotopy category.** In symmetric spectra, $\otimes^{\mathbf{L}}$ is the derived smash product, with unit the cofibrant replacement of the (non-cofibrant) sphere spectrum $\mathbb{S}$. The invariance clause shows that the many models of spectra (symmetric, orthogonal, $S$-modules) give *monoidally equivalent* homotopy categories, so "the smash product on the stable homotopy category" is model-independent. The non-obvious point is that without the *monoidal* refinement of Quillen equivalence, one would only get an equivalence of plain categories, not of monoidal ones.

**Spaces — the homotopy product and the failure of strict associativity made harmless.** In $\mathbf{sSet}$ or compactly generated spaces, $\otimes^{\mathbf{L}} = \times$ (everything is cofibrant in $\mathbf{sSet}$, so $\otimes^{\mathbf{L}} = \times$ on the nose). The theorem says the homotopy category of spaces is cartesian closed, with derived mapping spaces as internal hom. The application worth dwelling on is that even where the point-set product is strictly associative, the theorem's machinery is what guarantees the *homotopy* product and the derived mapping spaces assemble coherently — the framework that later supports $H$-spaces and loop-space theory.

---

# Bridges

- **[[Thm - The Pushout-Product and Pullback-Hom Form a Quillen Bifunctor|The Quillen bifunctor theorem]]** — the engine. That theorem supplies the well-defined, associative derived tensor and the derived internal hom; this theorem adds the unit (via the unit axiom) and assembles the coherence to make $\mathrm{Ho}(\mathcal{C})$ a *closed symmetric monoidal* category. The bifunctor theorem is the multiplication and the adjunction; this one is the full algebra including the unit.

- **[[Thm - The Homotopy Category of a Model Category|The fundamental theorem of model categories]]** — the substrate. That theorem builds $\mathrm{Ho}(\mathcal{C})$ itself, with morphisms as homotopy classes between bifibrant replacements; this theorem puts a monoidal structure on that homotopy category. The cofibrant replacements used to define $\otimes^{\mathbf{L}}$ are exactly the $Q$ from the fundamental theorem's construction.

- **[[Def - Closed Monoidal Category|Closed monoidal categories]]** — the un-homotopified target. The output of this theorem is an ordinary closed symmetric monoidal category $\mathrm{Ho}(\mathcal{C})$; everything you know about closed monoidal categories (self-enrichment, RAPL/LAPC, the internal hom as linear implication) applies to it. The derived internal hom $\mathbf{R}[-,-]$ is a genuine internal hom on $\mathrm{Ho}(\mathcal{C})$.

- **Tensor-triangulated categories** — the stable refinement. When $\mathcal{C}$ is also stable, the derived tensor makes $\mathrm{Ho}(\mathcal{C})$ a tensor-triangulated category: the symmetric monoidal structure of this theorem and the triangulation of the stable structure are compatible (the tensor is exact in each variable). The derived category $D(R)$ with $\otimes^{\mathbf{L}}_R$ and the stable homotopy category with $\wedge$ are the canonical examples, and Balmer's reconstruction of geometry from the tensor-triangular spectrum starts here.

---

# Unlocked by This

> [!tip] The Symmetric Monoidal Stable Homotopy Category *(from Stable Homotopy Theory)*
> Applied to spectra, this theorem produces the **stable homotopy category** as a symmetric monoidal category under the smash product, with unit the sphere spectrum. The invariance clause makes it model-independent. This is the object on which all of stable homotopy theory — generalized cohomology theories as ring spectra, the chromatic filtration, $E_\infty$-structures — is founded.

> [!tip] The Derived Category as a Tensor Category *(from Homological / Derived Algebra)*
> For $\mathbf{Ch}(R)$ this gives the **derived category** $D(R)$ its symmetric monoidal structure $\otimes^{\mathbf{L}}_R$ with internal hom $\mathbf{R}\mathrm{Hom}_R$, computing **Tor** and **Ext**. The same applies to the derived category of quasi-coherent sheaves on a **scheme**, whose monoidal structure underlies Fourier–Mukai theory and the modern study of derived categories in algebraic geometry.

> [!tip] Tannakian Reconstruction and Tensor-Triangular Geometry *(from Derived Algebraic Geometry)*
> Once $\mathrm{Ho}(\mathcal{C})$ is symmetric monoidal (and stable), one can reconstruct geometric objects from it: the Balmer spectrum recovers $\mathrm{Spec}$ from $D^{\mathrm{perf}}(R)$, and Tannakian-style theorems recover a scheme or stack from its symmetric monoidal category of (quasi-coherent) sheaves. The monoidal structure this theorem provides is the input to all such reconstruction.

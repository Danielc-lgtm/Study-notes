---
type: theorem
subject: category-theory
prereqs:
  - "Def - Equivalence of Categories"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
  - "Def - Natural Transformation"
  - "Thm - Functors Preserve Isomorphisms"
tags: [category-theory, foundations]
---

# Notation

$F : \mathcal{C} \to \mathcal{D}$ is a [[Def - Functor|functor]]; $G : \mathcal{D} \to \mathcal{C}$ a candidate quasi-inverse. An [[Def - Equivalence of Categories|equivalence]] is data $(F, G, \eta, \varepsilon)$ with [[Def - Natural Transformation|natural isomorphisms]] $\eta : 1_{\mathcal{C}} \cong GF$, $\varepsilon : FG \cong 1_{\mathcal{D}}$. The functor $F$ is [[Def - Full, Faithful, and Essentially Surjective Functor|full]] if each $\mathcal{C}(A,B) \to \mathcal{D}(FA,FB)$ is surjective, **faithful** if each is injective, **essentially surjective** if every $D \in \mathcal{D}$ admits an iso $FC \cong D$. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Statement

> **Theorem (Characterization of Equivalence).** A [[Def - Functor|functor]] $F : \mathcal{C} \to \mathcal{D}$ is an [[Def - Equivalence of Categories|equivalence of categories]] if and only if $F$ is [[Def - Full, Faithful, and Essentially Surjective Functor|full, faithful, and essentially surjective]].

The forward direction ($\Rightarrow$) is the easy half: an equivalence is automatically full, faithful, and essentially surjective. The reverse direction ($\Leftarrow$) is the substantive half: from a full, faithful, essentially surjective $F$ one *constructs* a quasi-inverse $G$ together with the natural [[Def - Isomorphism|isomorphisms]] — a construction that requires the **axiom of choice** (one chooses, for each object $D$ of $\mathcal{D}$, an object $GD$ of $\mathcal{C}$ and an isomorphism $FGD \cong D$).

---

# Motivation

[[Def - Equivalence of Categories|Equivalence]] is *defined* by exhibiting a quadruple $(F, G, \eta, \varepsilon)$, but in practice one almost never has the quasi-inverse $G$ in hand. What one usually has is a single functor $F$ and a feeling that it is "the right comparison" — the functor $\mathbf{Mat}_k \to \mathbf{FinVect}_k$, the inclusion of a [[Def - Subcategory|skeleton]], the [[Def - Functor|Spec]] functor. This theorem is what converts that feeling into a proof. It reduces the global, choice-laden task "produce a quasi-inverse and two natural isomorphisms" to three *local* checks on $F$ alone: is it injective on each hom-set, surjective on each hom-set, and does it reach every object up to iso?

The reduction is enormous in practice. Verifying full + faithful + essentially surjective never requires guessing the inverse functor; each condition is checked one hom-set or one object at a time. The theorem's reverse direction does the hard work once and for all — it shows that these three local conditions are *enough* to manufacture the inverse — so that every subsequent equivalence proof is three routine verifications. This is why the theorem is the working definition of equivalence, and why the four-tuple definition is rarely seen after this point.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition for the *useful* (⟸) direction is "$F$ is full, faithful, and essentially surjective". The source question is how these three conditions arrive disguised.

The first source is **a functor that is bijective on hom-sets by a dimension or degree count**. Faithfulness and fullness together say each $\mathcal{C}(A,B) \to \mathcal{D}(FA,FB)$ is a bijection; often this is verified by exhibiting both as sets of the same finite size, or by an explicit inverse formula. *Example problem:* $\mathbf{Mat}_k \to \mathbf{FinVect}_k$ is fully faithful because $n \times m$ matrices *are* the linear maps $k^m \to k^n$ — the bijection is the identity, suitably read.

The second source is **a "normal form" or "presentation" theorem supplying essential surjectivity**. Whenever every object of $\mathcal{D}$ can be put in a standard form coming from $\mathcal{C}$, that *is* essential surjectivity. *Example problem:* every finite-dimensional vector space has a basis, hence is isomorphic to some $k^n$ — the basis theorem is exactly the essential surjectivity of $\mathbf{Mat}_k \to \mathbf{FinVect}_k$.

The third source is **a fully faithful inclusion of a subcategory that meets every iso-class**. A full [[Def - Subcategory|subcategory]] inclusion is automatically fully faithful; if it additionally contains a representative of every isomorphism class, it is essentially surjective and hence an equivalence. *Example problem:* the inclusion of any [[Def - Subcategory|skeleton]] $\mathrm{sk}(\mathcal{C}) \hookrightarrow \mathcal{C}$ is an equivalence — full and faithful as a full subcategory, essentially surjective because every object is isomorphic to its representative.

**Targets (Output Amplification)**

Combine the conclusion with **the fact that equivalences preserve all categorical structure**. Once $F$ is known to be an equivalence, it transports [[Def - Isomorphism, Monomorphism, Epimorphism|isos, monos, epis]], [[Def - Limit and Colimit|limits and colimits]], initial/terminal objects, [[Def - Adjunction|adjunctions]] — everything expressible categorically. The further result $E$: a property is established in the easier of the two equivalent categories and transported to the other for free.

Combine the conclusion with **the existence of a quasi-inverse $G$**. The theorem does not merely assert $F$ is an equivalence; its proof *produces* $G$. Having $G$ explicitly lets you compute the inverse comparison, e.g. read off how $\mathbf{FinVect}_k \to \mathbf{Mat}_k$ acts (choose a basis of each space). The further result is a concrete two-way dictionary, not just an existence statement.

Combine the conclusion with **chains of equivalences**. Equivalence is transitive, so a composite of functors each shown to be an equivalence by this theorem is again an equivalence. The further result is multi-step transport: $\mathcal{A} \simeq \mathcal{B} \simeq \mathcal{C}$ established by three local checks at each stage.

---

# Why Is It True

The forward direction is a short computation: if $(F, G, \eta, \varepsilon)$ is an equivalence then the natural isomorphisms force $F$ to be fully faithful (the hom-set maps have inverses built from $G, \eta, \varepsilon$) and essentially surjective ($\varepsilon_D : FGD \cong D$ exhibits each $D$ as iso to something in the image). The interest is all in the reverse direction.

Here is the idea, and it is genuinely the only idea. We must build $G$ from $F$. **Essential surjectivity gives us, for each object $D$, at least one object $GD$ of $\mathcal{C}$ with $FGD \cong D$ — so we use the axiom of choice to pick one such $GD$ and one such isomorphism $\varepsilon_D : FGD \to D$.** That defines $G$ on objects and simultaneously defines the counit $\varepsilon$. Now we must define $G$ on morphisms. Given $h : D \to D'$, we want $Gh : GD \to GD'$. Transport $h$ across the chosen isomorphisms to a map $FGD \to FGD'$, namely $\varepsilon_{D'}^{-1} \circ h \circ \varepsilon_D$. **Full faithfulness now does the decisive work: this map between objects in the image of $F$ comes from a *unique* morphism $GD \to GD'$ in $\mathcal{C}$** — fullness supplies a preimage, faithfulness makes it unique — and that unique preimage is defined to be $Gh$. Functoriality of $G$ and the naturality of $\varepsilon$ then fall out of uniqueness. The unit $\eta : 1 \cong GF$ is obtained similarly, and it is an isomorphism because $F$ is fully faithful and hence (by [[Thm - Functors Preserve Isomorphisms|reflection of isos]]) reflects the iso visible after applying $F$.

**The mechanism in one line: essential surjectivity chooses the objects $GD$, and full faithfulness turns "morphisms between images" into "morphisms in $\mathcal{C}$" bijectively, which is exactly the data needed to make $G$ a functor and a quasi-inverse.** Fully faithfulness is doing two jobs — it defines $G$ on arrows, and it makes the unit an iso.

---

# What Makes This Hard

The proof is conceptually clean but has three places people stumble. First, the **axiom of choice** is unavoidable in the (⟸) direction and is easy to use without noticing: choosing $GD$ and $\varepsilon_D$ for *every* $D$ at once is a choice over a (possibly proper) class. Second, defining $G$ on morphisms requires recognizing that full faithfulness yields a *unique* lift, and it is the uniqueness (faithfulness) — not merely existence (fullness) — that makes $G$ well-defined and functorial; skipping the uniqueness check leaves $G$ ambiguous. Third, verifying that $\eta$ and $\varepsilon$ are *natural* (not just isomorphisms componentwise) is where the bookkeeping lives; the naturality squares follow from the uniqueness in the definition of $G$ on morphisms, and this is the step most often hand-waved.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** ($\Rightarrow$) compute that an equivalence is fully faithful and essentially surjective from $\eta, \varepsilon$. ($\Leftarrow$) use essential surjectivity + choice to define $G$ on objects (and the counit $\varepsilon$), use full faithfulness to define $G$ on morphisms uniquely, then verify $G$ is a functor and that $\eta, \varepsilon$ are natural isomorphisms.

**Subgoal decomposition:**

1. **($\Rightarrow$) Equivalence implies the three properties.** From $(F, G, \eta, \varepsilon)$, show $F$ is fully faithful and essentially surjective.
   - *Hint:* For essential surjectivity use $\varepsilon_D : FGD \cong D$. For full faithfulness, show $\mathcal{C}(A,B) \to \mathcal{D}(FA, FB)$ has an inverse built from $G$ and the naturality of $\eta$.
   - *Why needed:* It is the forward half and supplies the easy direction.

2. **($\Leftarrow$) Define $G$ on objects.** For each $D$, choose $GD \in \mathcal{C}$ and iso $\varepsilon_D : FGD \to D$.
   - *Hint:* This is exactly essential surjectivity plus the axiom of choice.
   - *Why needed:* It gives the object-assignment of $G$ and the counit simultaneously.

3. **($\Leftarrow$) Define $G$ on morphisms.** For $h : D \to D'$, define $Gh$ as the unique preimage under $F$ of $\varepsilon_{D'}^{-1} \circ h \circ \varepsilon_D$.
   - *Hint:* Full faithfulness: fullness gives a preimage, faithfulness makes it unique.
   - *Why needed:* Completes $G$ as a functor; uniqueness forces functoriality.

4. **($\Leftarrow$) Build the unit and check naturality.** Produce $\eta : 1_{\mathcal{C}} \cong GF$ and verify $\eta, \varepsilon$ natural.
   - *Hint:* $\eta_C$ is the unique morphism with $F\eta_C = \varepsilon_{FC}^{-1}$; it is an iso because $F$ reflects isos ([[Thm - Functors Preserve Isomorphisms]]). Naturality follows from uniqueness in subgoal 3.
   - *Why needed:* Supplies the remaining equivalence data and certifies it is coherent.

---

# Lemma Decomposition

> [!note]- Lemma 1: An equivalence is fully faithful and essentially surjective
> **Statement:** If $(F, G, \eta, \varepsilon)$ is an equivalence, then $F$ is full, faithful, and essentially surjective.
>
> **Hint:** Essential surjectivity is immediate from $\varepsilon$. For faithfulness, if $Ff = Ff'$ apply $G$ and conjugate by the natural iso $\eta$ to get $f = f'$. For fullness, given $k : FA \to FB$, transport $Gk$ back across $\eta$.
>
> **Why needed:** It is the entire forward direction.
>
> > [!note]- Full proof
> > *Essentially surjective:* for any $D$, $\varepsilon_D : FGD \to D$ is an iso, so $D \cong FGD = F(GD)$.
> >
> > *Faithful:* suppose $Ff = Ff'$ for $f, f' : A \to B$. Then $GFf = GFf'$. Naturality of $\eta : 1 \cong GF$ gives $GFf \circ \eta_A = \eta_B \circ f$ and $GFf' \circ \eta_A = \eta_B \circ f'$. Since $GFf = GFf'$, the left sides agree, so $\eta_B \circ f = \eta_B \circ f'$, and $\eta_B$ is an iso (hence mono), giving $f = f'$.
> >
> > *Full:* given $k : FA \to FB$, set $f := \eta_B^{-1} \circ Gk \circ \eta_A : A \to B$. A computation using naturality of $\eta$ shows $GFf = Gk$, and since $G$ is faithful (by the symmetric argument applied to $G$, using $\varepsilon$), $Ff = k$. Thus $F$ is full.

> [!note]- Lemma 2: Full faithfulness gives unique lifts of morphisms between images
> **Statement:** If $F$ is fully faithful, then for any $A, B \in \mathcal{C}$ and any morphism $k : FA \to FB$ there is a *unique* $f : A \to B$ with $Ff = k$.
>
> **Hint:** Fullness gives existence; faithfulness gives uniqueness.
>
> **Why needed:** This is the mechanism that defines $G$ on morphisms and forces $G$ to be a functor.
>
> > [!note]- Full proof
> > By fullness, the map $F_{A,B} : \mathcal{C}(A,B) \to \mathcal{D}(FA, FB)$ is surjective, so some $f$ has $Ff = k$. By faithfulness, $F_{A,B}$ is injective, so $f$ is unique. Hence $F_{A,B}$ is a bijection.

> [!note]- Lemma 3: The constructed $\eta$ is a natural isomorphism
> **Statement:** With $G$ defined as in the scaffold and $\eta_C$ the unique morphism with $F\eta_C = \varepsilon_{FC}^{-1} : FC \to FGFC$, the family $\eta = (\eta_C)$ is a natural isomorphism $1_{\mathcal{C}} \cong GF$.
>
> **Hint:** Each $F\eta_C$ is an iso, so each $\eta_C$ is an iso by reflection ([[Thm - Functors Preserve Isomorphisms]]); naturality follows from the uniqueness in Lemma 2 applied to the defining equation.
>
> **Why needed:** Supplies the unit and certifies the equivalence data is coherent.
>
> > [!note]- Full proof
> > By definition $F\eta_C = \varepsilon_{FC}^{-1}$, an isomorphism. Since $F$ is fully faithful it reflects isomorphisms ([[Thm - Functors Preserve Isomorphisms|corollary]]), so each $\eta_C$ is an iso. For naturality, take $f : C \to C'$; both $GFf \circ \eta_C$ and $\eta_{C'} \circ f$ have the same image under $F$ (compute both, using $F\eta = \varepsilon^{-1}$ and naturality of $\varepsilon$), so by faithfulness they are equal. Thus the naturality square commutes and $\eta$ is a natural isomorphism.

---

# Formal Proof

> [!note]- Complete formal proof
> **($\Rightarrow$)** By Lemma 1, an equivalence $(F, G, \eta, \varepsilon)$ has $F$ full, faithful, and essentially surjective.
>
> **($\Leftarrow$)** Suppose $F$ is full, faithful, and essentially surjective.
>
> **Step 0 — choices (axiom of choice).** For each object $D$ of $\mathcal{D}$, essential surjectivity provides some object of $\mathcal{C}$ whose image is isomorphic to $D$; choose one, call it $GD$, and choose an isomorphism $\varepsilon_D : FGD \xrightarrow{\sim} D$. This defines $G$ on objects and the family $\varepsilon = (\varepsilon_D)$.
>
> **Step 1 — $G$ on morphisms.** Given $h : D \to D'$, the morphism $\varepsilon_{D'}^{-1} \circ h \circ \varepsilon_D : FGD \to FGD'$ lies between images of $F$. By Lemma 2 there is a unique $Gh : GD \to GD'$ with $F(Gh) = \varepsilon_{D'}^{-1} \circ h \circ \varepsilon_D$. Define $Gh$ to be this morphism.
>
> **Step 2 — $G$ is a functor.** $F(G1_D) = \varepsilon_D^{-1} \circ 1_D \circ \varepsilon_D = 1_{FGD} = F(1_{GD})$, so by faithfulness $G1_D = 1_{GD}$. For composable $h, h'$, $F(Gh' \circ Gh) = F(Gh') \circ F(Gh) = (\varepsilon_{D''}^{-1} h' \varepsilon_{D'})(\varepsilon_{D'}^{-1} h \varepsilon_D) = \varepsilon_{D''}^{-1}(h' h)\varepsilon_D = F(G(h' h))$, so by faithfulness $G(h'h) = Gh' \circ Gh$. Thus $G : \mathcal{D} \to \mathcal{C}$ is a functor.
>
> **Step 3 — $\varepsilon$ is a natural isomorphism $FG \cong 1_{\mathcal{D}}$.** Each $\varepsilon_D$ is an iso by construction. Naturality: for $h : D \to D'$, $\varepsilon_{D'} \circ FG(h) = \varepsilon_{D'} \circ (\varepsilon_{D'}^{-1} \circ h \circ \varepsilon_D) = h \circ \varepsilon_D$, which is the naturality square. So $\varepsilon : FG \xrightarrow{\sim} 1_{\mathcal{D}}$.
>
> **Step 4 — $\eta$ is a natural isomorphism $1_{\mathcal{C}} \cong GF$.** Define $\eta_C : C \to GFC$ as the unique morphism with $F\eta_C = \varepsilon_{FC}^{-1} : FC \to FGFC$ (Lemma 2 applied to the iso $\varepsilon_{FC}^{-1}$). By Lemma 3, $\eta = (\eta_C)$ is a natural isomorphism $1_{\mathcal{C}} \xrightarrow{\sim} GF$.
>
> The data $(F, G, \eta, \varepsilon)$ is therefore an equivalence of categories. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Finite-dimensional vector spaces and matrices.** Show $\mathbf{Mat}_k \to \mathbf{FinVect}_k$ (objects $n \mapsto k^n$, matrices to linear maps) is full, faithful, and essentially surjective, hence an equivalence — without ever writing down the inverse functor. Essential surjectivity is the existence of bases; full faithfulness is "matrices are linear maps". This is the canonical application.

**Stone duality.** The category of Boolean algebras is equivalent to the opposite of the category of Stone spaces (compact, Hausdorff, totally disconnected). Proving the comparison functor is full, faithful, and essentially surjective is exactly an instance of this theorem, and it is the template for all "concrete vs. spatial" dualities, including $\mathbf{CRing}^{\mathrm{op}} \simeq$ affine schemes.

**Representations and [[Def - Module|modules]].** For a [[Def - Group|group]] $G$ and field $k$, the category of $k$-linear representations of $G$ is equivalent to the category of modules over the group algebra $k[G]$. Verify the comparison functor (a representation *is* a $k[G]$-module) is fully faithful and essentially surjective; this is how representation theory is absorbed into module theory.

---

# Bridges

- **[[Thm - Functors Preserve Isomorphisms|Functors Preserve Isomorphisms]]** — its corollary (fully faithful functors reflect isos) is used in Step 4 to show $\eta$ is a natural *isomorphism*: each $\eta_C$ becomes an iso the instant $F\eta_C$ is, precisely because $F$ is fully faithful. The two theorems are proved in sequence for this reason.

- **[[Def - Subcategory|Skeleton]]** — the cleanest source of equivalences. A skeleton inclusion is full and faithful (full subcategory) and essentially surjective (one representative per iso-class), so it is an equivalence by this theorem; conversely two categories are equivalent iff their skeletons are isomorphic, isolating the iso-vs-equal slack.

- **[[Def - Adjunction|Adjoint equivalence]]** — one can always upgrade an equivalence to an *adjoint* equivalence, where $\eta$ and $\varepsilon$ additionally satisfy the triangle identities, making $F$ both left and right adjoint to $G$. The construction in Step 4 can be massaged so that the equivalence is simultaneously an [[Def - Adjunction|adjunction]] — the bridge to Chapter IV.

---

# Unlocked by This

> [!tip] Morita Theory and Derived Equivalence *(from Ring Theory and Homological Algebra)*
> Recognizing equivalences via "fully faithful + essentially surjective" is the working tool behind **Morita equivalence** ($\mathbf{Mod}_R \simeq \mathbf{Mod}_S$) and **derived equivalence** ($D^b(\mathcal{A}) \simeq D^b(\mathcal{B})$). One exhibits a comparison functor and checks the three local conditions, never the quasi-inverse directly.

> [!tip] Tannaka Reconstruction and the Functor of Points *(from Algebraic Geometry and Representation Theory)*
> Reconstruction theorems — recovering a group from its category of representations (Tannaka), or a scheme from its [[Def - Functor|functor of points]] — assert that a certain functor is an equivalence onto its essential image, verified by this characterization. "Full, faithful, essentially surjective" is the recurring signature of a reconstruction.

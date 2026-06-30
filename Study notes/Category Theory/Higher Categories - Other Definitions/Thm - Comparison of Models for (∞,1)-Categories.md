---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Quasi-Category"
  - "Def - Segal Category and Complete Segal Space"
  - "Def - Enriched Category"
  - "Def - Model Category"
  - "Def - Quillen Adjunction and Quillen Equivalence"
tags: [category-theory, higher-categories, foundations]
---

# Notation

An **$(\infty,1)$-category** is a higher category with cells in every dimension, all invertible above dimension $1$ — the homotopy-theoretic generalisation of an ordinary category. A **model** of $(\infty,1)$-categories is a category $\mathcal{M}$ of presentations together with a [[Def - Model Category|model structure]] whose homotopy theory is "the homotopy theory of $(\infty,1)$-categories". The five models compared here:
- $\mathbf{sSet}_{\mathrm{Joyal}}$ — **[[Def - Quasi-Category|quasi-categories]]**: [[Def - Simplicial Set|simplicial sets]] with the Joyal model structure; fibrant objects are quasi-categories.
- $\mathbf{sCat}_{\mathrm{Bergner}}$ — **simplicial categories**: categories **[[Def - Enriched Category|enriched]]** in [[Def - Simplicial Set|simplicial sets]], with the Bergner model structure.
- $\mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{Rezk}}$ — **complete Segal spaces**: simplicial spaces with the Rezk (complete Segal) model structure ([[Def - Segal Category and Complete Segal Space]]).
- $\mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{SeCat}}$ — **Segal categories**: simplicial spaces with discrete object-space, with the projective/injective Segal-category model structure.
- $\mathbf{RelCat}$ — **relative categories**: pairs $(\mathcal{C}, \mathcal{W})$ of a category with a marked subcategory of weak equivalences, with the Barwick–Kan model structure.
We write $\dashv$ for adjunction, $\simeq$ for Quillen equivalence, $\mathfrak{C}$ for the **homotopy-coherent nerve**'s left adjoint, $N^{\mathrm{hc}}$ for the homotopy-coherent nerve, and $\mathrm{Map}(X,Y)$ for the **derived mapping space**. The full registry is on [[Higher Categories — Other Definitions of Weak n-Categories]].

---

# Statement

> **Comparison Theorem (Bergner–Joyal–Lurie–Barwick–Kan).** The five model categories
> $$
> \mathbf{sSet}_{\mathrm{Joyal}}, \quad \mathbf{sCat}_{\mathrm{Bergner}}, \quad \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{Rezk}}, \quad \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{SeCat}}, \quad \mathbf{RelCat}
> $$
> are connected by a web of [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalences]]. In particular:
> $$
> \mathfrak{C} : \mathbf{sSet}_{\mathrm{Joyal}} \;\xrightarrow{\;\simeq\;}\; \mathbf{sCat}_{\mathrm{Bergner}} : N^{\mathrm{hc}}
> $$
> (the [[Def - Homotopy|homotopy]]-coherent nerve adjunction, Lurie) is a Quillen equivalence; quasi-categories, complete Segal spaces, and Segal categories are connected by Quillen equivalences (Joyal–Tierney); Segal categories and complete Segal spaces sit in a chain of equivalences with simplicial categories (Bergner); and relative categories are Quillen equivalent to complete Segal spaces (Barwick–Kan). Consequently all five present **the same** homotopy theory: a single $(\infty,1)$-category $\mathbf{Cat}_\infty$, the "$\infty$-category of $\infty$-categories". Any homotopy-invariant statement proved in one model holds in all.

---

# Motivation

This is the theorem that rescues the subject from its own embarrassment of riches. By the time the comparison was completed, there were five or six serious, independently-motivated definitions of "$(\infty,1)$-category" — quasi-categories from Boardman–Vogt and Joyal, simplicial categories from Dwyer–Kan, complete Segal spaces from Rezk, Segal categories from Hirschowitz–Simpson, relative categories from Barwick–Kan. Each came with its own literature, its own constructions, its own community. The obvious and pressing worry was whether these were *the same subject* or merely cousins that happened to agree in easy cases. If they disagreed, the field would fracture; theorems proved for quasi-categories would have unknown status for complete Segal spaces, and the foundational question "what is an $\infty$-category" would have no answer.

The comparison theorem says they are the same subject, in the strongest possible sense: the model categories are *Quillen equivalent*, so they have not just equivalent homotopy categories but equivalent homotopy *theories* — equivalent derived mapping spaces, equivalent diagram categories, equivalent everything that is homotopy-invariant. The practical consequence is the daily working method of every $\infty$-categorist: **prove it where it is easiest, transport it everywhere.** Limits and colimits are cleanest in quasi-categories; enrichment and explicit mapping spaces are cleanest in simplicial categories; the treatment of equivalences and the relation to model categories is cleanest in complete Segal spaces and relative categories. The theorem licenses moving freely among them. It is the reason a modern paper can say "$\infty$-category" without specifying a model, and the reason Riehl–Verity's *model-independent* theory is even possible.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "two of the standard model structures plus an adjunction between them"; the skill is recognising when a comparison you need is an instance.

The first disguised source is **a forgetful/nerve functor between two kinds of presentation that you suspect loses no homotopical information**. Whenever you have a functor from one model to another — a nerve, a realisation, an inclusion — that is the *candidate* left or right adjoint of a Quillen equivalence. The non-obvious step is to *identify its adjoint* and recognise the pair as one of the comparison equivalences. *Example problem:* given a simplicial category, produce a quasi-category via the homotopy-coherent nerve $N^{\mathrm{hc}}$, and recognise that the comparison theorem guarantees this is an equivalence, so the two carry the same mapping spaces.

The second disguised source is **a construction performed in one model that you need in another**. If you have built, say, a limit or an adjunction of quasi-categories, and a colleague's argument is phrased for complete Segal spaces, the comparison provides the translation. The non-obvious recognition is that *the construction is homotopy-invariant*, so it transports along the Quillen equivalence automatically. *Example problem:* transport the straightening/unstraightening equivalence (a theorem about quasi-categories) to complete Segal spaces by composing with the comparison.

The third disguised source is **a model category in the wild that you want to view as an $(\infty,1)$-category**. Any [[Def - Model Category|model category]], or even any [[Def - Quillen Adjunction and Quillen Equivalence|relative category]] $(\mathcal{C},\mathcal{W})$, presents an $(\infty,1)$-category via the Barwick–Kan equivalence $\mathbf{RelCat} \simeq \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{Rezk}}$. The non-obvious step is that you do *not* need the full model structure — the bare data of weak equivalences suffices to extract the $(\infty,1)$-category. *Example problem:* show that the $(\infty,1)$-category presented by $(\mathbf{Top}, \text{weak equivalences})$ agrees with the quasi-category $\mathrm{Sing}$-construction by routing both through the comparison.

**Targets (Output Amplification)**

The bare conclusion is "the five models are Quillen equivalent". Combined with other facts it does much more.

Combine the conclusion with **a theorem proved in one model**. Since a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] induces an equivalence of homotopy theories, any homotopy-invariant theorem — existence of limits, the adjoint functor theorem for $\infty$-categories, the Yoneda lemma — proved for quasi-categories holds verbatim for the other models. The further result $E$ is *theorem portability*: the entire content of Lurie's *Higher Topos Theory* (written for quasi-categories) becomes available for complete Segal spaces for free. This is non-obvious because the proofs do not transport — only the *statements* do, via the equivalence.

Combine the conclusion with **the homotopy hypothesis**. The [[Thm - The Homotopy Hypothesis|homotopy hypothesis]] identifies $(\infty,0)$-categories (groupoids) with spaces; the comparison theorem identifies the models of $(\infty,1)$-categories. Together they give a coherent ladder: spaces $\subset$ $(\infty,1)$-categories, with both rungs model-independent. The further result is that the **core** (maximal sub-$\infty$-groupoid) of any model of an $(\infty,1)$-category is a space, computed the same way in every model. This is useful because it connects the two foundational theorems of the chapter into one picture.

Combine the conclusion with **a monoidal or enriched structure**. The models can be compared *compatibly with monoidal structure* (Lurie), so the $(\infty,1)$-category of $\infty$-categories is itself symmetric monoidal in a model-independent way, and enrichment over it is well-defined. The further result $E$ is that **stable $\infty$-categories**, **monoidal $\infty$-categories**, and module structures are all model-independent. This is non-obvious because monoidal structures are notoriously sensitive to strictification, yet the comparison can be made to respect them.

---

# Why Is It True

The reason all these models agree is that they are all encoding the *same* data — objects, mapping spaces, and homotopy-coherent composition — and merely *bookkeeping* it differently. Look at what each one records. A simplicial category records the mapping spaces *directly* as hom-simplicial-sets, with strict composition. A complete Segal space records them as the fibres of $X_1 \to X_0 \times X_0$, with composition encoded by the Segal condition. A quasi-category records them implicitly: the mapping space between $x$ and $y$ is recovered as a space of $1$-simplices-with-fixed-endpoints, and composition is the inner-horn fillers. A relative category records the *least* data — just which maps are equivalences — and reconstructs the mapping spaces by hammock localisation. These are four ways to write down one structure.

> Every model of an $(\infty,1)$-category is a way of recording *objects, derived mapping spaces, and coherent composition*; the comparison functors are the dictionaries translating one bookkeeping scheme into another, and they are equivalences because the underlying data — the mapping spaces and their composition — is the same in all of them.

The technical heart, then, is to check that each translation functor *preserves the mapping spaces up to weak equivalence*. This is exactly what the Quillen-equivalence conditions verify: the derived unit and counit being weak equivalences says precisely that translating from model $A$ to model $B$ and back recovers the original mapping spaces and composition up to coherent homotopy. The hardest single comparison, Lurie's $\mathfrak{C} \dashv N^{\mathrm{hc}}$ between quasi-categories and simplicial categories, is hard for one specific reason: the left adjoint $\mathfrak{C}$ must build, from a quasi-category, an honest simplicial category whose mapping spaces are the *correct* derived mapping spaces — and computing $\mathfrak{C}(\Delta^n)$ requires understanding the "necklace" combinatorics that turn inner-horn-fillers into a strict composition. Once you know $\mathfrak{C}(\Delta^n)$ has the right mapping spaces (cubes, hence contractible), the equivalence follows because both sides compute the same mapping spaces on the generators and the model structures propagate this to everything.

---

# What Makes This Hard

The difficulty is almost entirely in the *left adjoints* of the comparison functors and in computing their derived mapping spaces. The nerve-type *right* adjoints (the homotopy-coherent nerve, the classification diagram) are easy to write down; the trouble is their left adjoints, which must *strictify* homotopy-coherent data — and the computation of $\mathfrak{C}(\Delta^n)$, the rigidification of the standard simplex, is the famous technical knot (its mapping spaces are cubes, but seeing this requires the "necklace" description of Dugger–Spivak). The most common error is to assume that a functor which is obviously an equivalence on homotopy *categories* is therefore a Quillen equivalence; it is not enough — one must check the derived *mapping spaces* agree, i.e. that the equivalence is "fully faithful at the spectral level", not merely on $\pi_0$. Many plausible comparison functors induce an equivalence of homotopy categories while failing to be Quillen equivalences, and distinguishing the two is the crux.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the proof strategy.**

**High-level strategy:**
For each adjacent pair of models, exhibit an adjunction, prove it is Quillen (left adjoint preserves cofibrations and trivial cofibrations), and prove it is an equivalence by showing the derived unit and counit are weak equivalences — which reduces to checking the comparison preserves derived mapping spaces. Chain the pairwise equivalences to connect all five.

**Subgoal decomposition:**

1. **Choose the spanning tree.** Fix the chain $\mathbf{sCat} \leftrightarrow \mathbf{sSet}_{\mathrm{Joyal}} \leftrightarrow \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{Rezk}} \leftrightarrow \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{SeCat}}$ and $\mathbf{RelCat} \leftrightarrow \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{Rezk}}$.
   - *Hint:* It suffices to connect the models into one tree; transitivity of Quillen equivalence does the rest.
   - *Why needed:* Reduces a complete web to finitely many pairwise comparisons.

2. **Quasi-categories ↔ simplicial categories.** Show $\mathfrak{C} \dashv N^{\mathrm{hc}}$ is Quillen and compute $\mathfrak{C}(\Delta^n)$.
   - *Hint:* $N^{\mathrm{hc}}$ is right Quillen by checking it sends [[Def - Fibration|fibrations]] and trivial fibrations correctly; the equivalence reduces to $\mathfrak{C}(\Delta^n)$ having cube (contractible) mapping spaces.
   - *Why needed:* This is the keystone comparison; it ties the most-used model to the most explicit one.

3. **Quasi-categories ↔ complete Segal spaces ↔ Segal categories.** Use Joyal–Tierney's two adjunctions ($p_1^*$ and $i_1^*$).
   - *Hint:* Both are induced by restriction/realisation along the two ways of viewing a bisimplicial set; check each is a Quillen equivalence by the mapping-space criterion.
   - *Why needed:* Connects the simplicial and bisimplicial worlds.

4. **Relative categories ↔ complete Segal spaces.** Use the classification diagram $N(\mathcal{C},\mathcal{W})$.
   - *Hint:* Barwick–Kan show the classification-diagram functor is the right adjoint of a Quillen equivalence.
   - *Why needed:* Brings the minimal-data model into the web and connects to model categories.

5. **Conclude by transitivity.** A composite of Quillen equivalences is a Quillen equivalence; all five are connected.
   - *Hint:* Derived functors compose.
   - *Why needed:* Upgrades the spanning tree to "all models present the same homotopy theory".

---

# Lemma Decomposition

> [!note]- Lemma 1: A Quillen equivalence is detected by derived mapping spaces
> **Statement:** A Quillen adjunction $F \dashv G$ between model categories is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] if and only if for all cofibrant $X$ and fibrant $Y$ a map $FX \to Y$ is a weak equivalence iff its adjunct $X \to GY$ is — equivalently, the derived unit and counit are weak equivalences.
>
> **Hint:** Unwind the definition of Quillen equivalence; the two-out-of-three property converts the adjunct condition into the unit/counit condition.
>
> **Why needed:** It reduces every comparison to a statement about mapping spaces, which is checkable on generators.
>
> > [!note]- Full proof
> > By definition $F \dashv G$ is a Quillen equivalence when, for cofibrant $X$ and fibrant $Y$, a map $f : FX \to Y$ is a weak equivalence in the target iff its adjunct $f^\flat : X \to GY$ is a weak equivalence in the source. Taking $Y$ a fibrant replacement of $FX$ and $f$ the replacement map shows the derived unit $X \to GFX^{\mathrm{fib}}$ is a weak equivalence; dually for the counit. Conversely, derived unit and counit being weak equivalences gives the adjunct criterion by two-out-of-three applied to the naturality square. Thus the two formulations coincide, and both are statements that $F$ preserves derived mapping spaces: $\mathrm{Map}(X,X') \simeq \mathrm{Map}(FX, FX')$. $\square$

> [!note]- Lemma 2: The homotopy-coherent nerve is right Quillen
> **Statement:** The homotopy-coherent nerve $N^{\mathrm{hc}} : \mathbf{sCat}_{\mathrm{Bergner}} \to \mathbf{sSet}_{\mathrm{Joyal}}$, right adjoint to rigidification $\mathfrak{C}$, sends fibrant simplicial categories (those locally Kan) to quasi-categories and preserves (trivial) fibrations.
>
> **Hint:** $N^{\mathrm{hc}}(\mathcal{D})_n = \mathbf{sCat}(\mathfrak{C}(\Delta^n), \mathcal{D})$; a locally-Kan $\mathcal{D}$ makes inner horns fill.
>
> **Why needed:** It establishes the keystone adjunction is Quillen, the precondition for the keystone equivalence.
>
> > [!note]- Full proof
> > By adjunction $N^{\mathrm{hc}}(\mathcal{D})_n = \mathbf{sCat}(\mathfrak{C}[\Delta^n], \mathcal{D})$. An inner horn $\Lambda^n_i \to N^{\mathrm{hc}}(\mathcal{D})$ corresponds to a map $\mathfrak{C}[\Lambda^n_i] \to \mathcal{D}$, and $\mathfrak{C}[\Lambda^n_i] \hookrightarrow \mathfrak{C}[\Delta^n]$ is a [[Def - Enriched Category|simplicial-categorical]] inclusion that is bijective on objects and a trivial cofibration on mapping spaces when $0 < i < n$ (the missing data is a retract of contractible cube faces). Since $\mathcal{D}$ is locally Kan, the lift exists, so $N^{\mathrm{hc}}(\mathcal{D})$ is a quasi-category. The same adjunction argument on the generating (trivial) fibrations shows $N^{\mathrm{hc}}$ is right Quillen. $\square$

> [!note]- Lemma 3: Rigidification has the correct mapping spaces
> **Statement:** For the standard simplex, the mapping spaces of $\mathfrak{C}[\Delta^n]$ are cubes: $\mathfrak{C}[\Delta^n](i,j) \cong (\Delta^1)^{j-i-1}$ for $i \le j$ (and empty for $i > j$), each of which is contractible.
>
> **Hint:** Use the "necklace" description: a point of $\mathfrak{C}[\Delta^n](i,j)$ is a subset of $\{i+1, \dots, j-1\}$, i.e. a vertex of a cube, with the simplicial structure filling it to $(\Delta^1)^{j-i-1}$.
>
> **Why needed:** Contractible (cube) mapping spaces on generators are exactly what forces the keystone adjunction to be a Quillen equivalence.
>
> > [!note]- Full proof
> > $\mathfrak{C}[\Delta^n]$ has objects $0,\dots,n$, and its mapping space from $i$ to $j$ is the nerve of the poset of subsets $S$ with $\{i,j\} \subseteq S \subseteq \{i,i+1,\dots,j\}$, ordered by inclusion. Such an $S$ is determined by the subset $S \cap \{i+1,\dots,j-1\}$ of the $(j-i-1)$-element set of "intermediate" indices, and the poset of all subsets of a $k$-element set is the face poset of the $k$-cube, whose nerve is $(\Delta^1)^k$. Hence $\mathfrak{C}[\Delta^n](i,j) \cong (\Delta^1)^{j-i-1}$, a contractible cube; composition is union of subsets. Because the mapping spaces are contractible exactly as the inner-horn fillers of $\Delta^n$ predict, the derived unit and counit of $\mathfrak{C} \dashv N^{\mathrm{hc}}$ are weak equivalences. $\square$

---

# Formal Proof

> [!note]- Complete formal proof (keystone comparison; web by transitivity)
> We prove the keystone Quillen equivalence $\mathfrak{C} : \mathbf{sSet}_{\mathrm{Joyal}} \rightleftarrows \mathbf{sCat}_{\mathrm{Bergner}} : N^{\mathrm{hc}}$ in full and indicate how the remaining comparisons assemble the web.
>
> **Step 0 — the model structures exist.** The Joyal model structure on $\mathbf{sSet}$ (cofibrations $=$ monos, fibrant objects $=$ [[Def - Quasi-Category|quasi-categories]]) and the Bergner model structure on $\mathbf{sCat}$ (weak equivalences $=$ Dwyer–Kan equivalences, fibrant objects $=$ locally Kan simplicial categories) are established model structures; we take them as given.
>
> **Step 1 — the adjunction.** Rigidification $\mathfrak{C}$ is the left Kan extension of $[n] \mapsto \mathfrak{C}[\Delta^n]$ along the Yoneda embedding, with right adjoint the homotopy-coherent nerve $N^{\mathrm{hc}}(\mathcal{D})_n = \mathbf{sCat}(\mathfrak{C}[\Delta^n], \mathcal{D})$. So $\mathfrak{C} \dashv N^{\mathrm{hc}}$.
>
> **Step 2 — it is a Quillen adjunction.** By Lemma 2, $N^{\mathrm{hc}}$ sends fibrant objects to quasi-categories and preserves (trivial) fibrations, so it is right Quillen and $\mathfrak{C}$ is left Quillen.
>
> **Step 3 — the derived unit/counit are equivalences.** By Lemma 3, $\mathfrak{C}[\Delta^n]$ has contractible cube mapping spaces, matching the derived mapping spaces of $\Delta^n$ as a quasi-category. Hence on the generators the comparison preserves derived mapping spaces; by Lemma 1 and propagation along the (cofibrantly generated) model structures, the derived unit $X \to N^{\mathrm{hc}}\mathfrak{C}(X)$ and counit $\mathfrak{C}N^{\mathrm{hc}}(\mathcal{D}) \to \mathcal{D}$ are weak equivalences for cofibrant $X$ / fibrant $\mathcal{D}$.
>
> **Step 4 — keystone conclusion.** By Lemma 1, $\mathfrak{C} \dashv N^{\mathrm{hc}}$ is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]]: $\mathbf{sSet}_{\mathrm{Joyal}} \simeq \mathbf{sCat}_{\mathrm{Bergner}}$.
>
> **Step 5 — the rest of the web.** Joyal–Tierney provide Quillen equivalences $\mathbf{sSet}_{\mathrm{Joyal}} \simeq \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{Rezk}}$ (via $t_!$ / restriction) and $\mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{SeCat}} \simeq \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{Rezk}}$; Bergner connects Segal categories to simplicial categories; Barwick–Kan give $\mathbf{RelCat} \simeq \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{Rezk}}$ via the classification diagram. Each is a Quillen equivalence by the same mapping-space criterion (Lemma 1).
>
> **Step 6 — conclude.** A composite of Quillen equivalences is a Quillen equivalence (derived functors compose and preserve weak equivalences). The five model categories are therefore connected into a single homotopy theory; they all present $\mathbf{Cat}_\infty$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Derived categories done right (homological algebra).** The naive **derived category** $D(R)$ of a [[Def - Ring|ring]] is a triangulated category with well-known defects: cones are not functorial, and there are no mapping *spaces*, only Hom-*sets*. Realise $D(R)$ instead as the homotopy category of the $(\infty,1)$-category presented by (chain complexes, quasi-[[Def - Isomorphism|isomorphisms]]) as a [[Def - Quillen Adjunction and Quillen Equivalence|relative category]], and use the comparison theorem to compute its derived mapping spaces $\mathrm{Map}(X,Y)$ in whichever model is convenient. The application is non-obvious because the same triangulated category arises from a much richer $(\infty,1)$-category, and the comparison says the enrichment is model-independent.

**Spaces with [[Def - Group|group]] action (equivariant homotopy theory).** The $(\infty,1)$-category of $G$-spaces can be presented as a simplicial category (with mapping spaces of equivariant maps) or as a quasi-category (via the equivariant singular complex). Use the comparison to show these agree, so that equivariant homotopy limits computed in one model match those in the other. The non-obvious recognition is that the *choice* of equivariant model (genuine vs. naive) is a choice of *which* $(\infty,1)$-category, but for a fixed choice the *model* is immaterial.

**Logic: the $\infty$-category of types (type theory).** A model of homotopy type theory presents an $(\infty,1)$-category (indeed an **∞-topos**) of types and functions. Use the comparison theorem to argue that the semantics is independent of whether one models types as simplicial sets, simplicial categories, or complete Segal spaces — so the *meaning* of a type-theoretic statement does not depend on the chosen categorical semantics. The application is non-obvious because it grounds the robustness of type-theoretic semantics in a purely homotopy-theoretic comparison theorem.

---

# Bridges

- **[[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] as the certificate of agreement** — the whole theorem is a statement that certain adjunctions are Quillen equivalences. A Quillen equivalence is stronger than an equivalence of homotopy categories: it requires the derived unit and counit to be weak equivalences, which forces *all* derived mapping spaces to agree, not just $\pi_0$. This is why the theorem says the models present the same *homotopy theory* and not merely the same homotopy category — the bridge is the precise sense in which "equivalent" is meant.

- **[[Thm - The Homotopy Category of a Model Category|Localisation of a model category]]** — every model category presents an $(\infty,1)$-category, namely its underlying relative category's image under $\mathbf{RelCat} \simeq \mathbf{ss}\text{-}\mathbf{Set}_{\mathrm{Rezk}}$. So the comparison theorem is what makes "the $(\infty,1)$-category presented by a model category" a well-defined notion independent of the presentation. The bridge: model categories are the *engineering*, and the comparison theorem certifies that different engineerings of the same homotopy theory yield the same $(\infty,1)$-category.

- **The [[Thm - The Homotopy Hypothesis|homotopy hypothesis]]** — the $(\infty,0)$ analogue and special case. Restricting all five models to their *groupoidal* objects (every morphism an equivalence) and applying the comparison gives five model-independent presentations of *spaces*, recovering the homotopy hypothesis. The two theorems are the two foundational rungs: $(\infty,0) =$ spaces (homotopy hypothesis), and $(\infty,1)$ model-independent (comparison theorem).

- **Model-independent ∞-category theory (Riehl–Verity)** — the theorem's natural sequel. Once the models are known equivalent, one axiomatises the common features in an **∞-cosmos** and develops adjunctions, limits, and the Yoneda lemma synthetically, never choosing a model. The comparison theorem is the licence: a synthetic result holds in every model because the models are Quillen equivalent. The bridge is that the comparison theorem turns "which model?" into a non-question, which is exactly the hypothesis the model-independent theory needs.

---

# Unlocked by This

> [!tip] Higher Topos Theory and ∞-Topoi *(from Higher Algebra / Algebraic Geometry)*
> With the models known equivalent, Lurie's foundations (built on [[Def - Quasi-Category|quasi-categories]]) develop **$\infty$-topoi** — $(\infty,1)$-categories of $\infty$-sheaves — the setting for **derived algebraic geometry** and the correct home of the **derived category** of a scheme. The comparison theorem guarantees the resulting theory is model-independent.

> [!tip] Stable ∞-Categories and Spectra *(from Higher Algebra)*
> The model-independence extends to *stable* $(\infty,1)$-categories — pointed $\infty$-categories where suspension is an equivalence — which are the $\infty$-categorical refinement of **triangulated categories** and the home of **spectra**. The comparison theorem ensures the stable $\infty$-category of spectra is the same object whether built from quasi-categories, simplicial categories, or complete Segal spaces.

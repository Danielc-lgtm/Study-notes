---
type: definition
subject: category-theory
prereqs:
  - "Def - Functor"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, foundations]
---

# Notation

Throughout, $F : \mathcal{C} \to \mathcal{D}$ is a [[Def - Functor|functor]]. For objects $A, B$ of $\mathcal{C}$, the **action on hom-sets** is the function
$$F_{A,B} : \mathcal{C}(A, B) \longrightarrow \mathcal{D}(FA, FB), \qquad f \mapsto Ff.$$
This is a compound page: it defines three interlocking properties of a functor — **faithful**, **full**, **essentially surjective** — because together they characterize when a functor is an [[Def - Equivalence of Categories|equivalence of categories]] ([[Thm - Characterization of Equivalence]]), and each is meaningless for the comparison without the others. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

A [[Def - Functor|functor]] does two things: it acts on objects and it acts on morphisms. To understand *how well* a functor reflects the source category inside the target, we ask three independent questions about these actions, and the answers give exactly the three properties on this page.

First question: does the functor *lose* morphisms — can it send two different arrows to the same arrow? If $F_{A,B}$ is **injective** for all $A, B$, the functor does not collapse morphisms, and we call it **faithful**. A faithful functor remembers how to tell arrows apart. The [[Def - Functor|forgetful functor]] $\mathbf{Grp} \to \mathbf{Set}$ is faithful: two distinct homomorphisms have distinct underlying functions. Faithfulness is what lets us treat the objects of $\mathcal{C}$ as "sets with structure and structure-preserving maps" — it is the precise meaning of "concrete category".

Second question: does the functor *invent* morphisms — are there arrows between $FA$ and $FB$ that do not come from arrows between $A$ and $B$? If $F_{A,B}$ is **surjective** for all $A, B$, every downstairs arrow lifts, and we call $F$ **full**. The forgetful functor $\mathbf{Grp} \to \mathbf{Set}$ is *not* full: most functions between underlying sets are not homomorphisms, so there are arrows in $\mathbf{Set}$ with no preimage. Fullness says $F$ does not see "extra" maps in the target.

A functor that is both full and faithful — **fully faithful** — induces a *bijection* on each hom-set: $\mathcal{C}(A, B) \cong \mathcal{D}(FA, FB)$. This is the strongest possible relationship between hom-sets short of an isomorphism of categories. A fully faithful functor embeds $\mathcal{C}$ into $\mathcal{D}$ as a full [[Def - Subcategory|subcategory]] (on the image objects), and a key consequence — proved on [[Thm - Functors Preserve Isomorphisms]] — is that it **reflects isomorphisms**: if $Ff$ is an iso then $f$ already was.

Third question, now about objects: does the functor *reach* every object — is every object of $\mathcal{D}$ at least isomorphic to something in the image of $F$? Note we ask for "isomorphic to", not "equal to", because in category theory equality of objects is the wrong notion — only isomorphism is. A functor with this property is **essentially surjective**. Why "essentially"? Because demanding $F$ hit every object *on the nose* is far too strong: it would distinguish isomorphic objects, which is exactly what categorical reasoning refuses to do. **The slack between "surjective on objects" and "essentially surjective on objects" is the entire difference between isomorphism and [[Def - Equivalence of Categories|equivalence]] of categories.**

These three properties are independent, and together — full $+$ faithful $+$ essentially surjective — they say $F$ is "the same as an isomorphism, up to the iso-vs-equal slack on objects", which is precisely [[Thm - Characterization of Equivalence|the characterization of an equivalence]]. That theorem is the reason this compound page exists.

---

# The Definition

Let $F : \mathcal{C} \to \mathcal{D}$ be a [[Def - Functor|functor]].

**Faithful.** $F$ is **faithful** if each action on hom-sets $F_{A,B} : \mathcal{C}(A, B) \to \mathcal{D}(FA, FB)$ is injective: for parallel morphisms $f, g : A \to B$, $Ff = Fg \implies f = g$.

**Full.** $F$ is **full** if each $F_{A,B}$ is surjective: for every morphism $h : FA \to FB$ in $\mathcal{D}$ there is $f : A \to B$ in $\mathcal{C}$ with $Ff = h$.

**Fully faithful.** $F$ is **fully faithful** if it is both full and faithful, equivalently if each $F_{A,B}$ is a bijection.

**Essentially surjective (on objects).** $F$ is **essentially surjective** if for every object $D$ of $\mathcal{D}$ there is an object $C$ of $\mathcal{C}$ and an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]] $FC \cong D$ in $\mathcal{D}$.

Note that fullness and faithfulness constrain the action on *morphisms* (per hom-set), while essential surjectivity constrains the reach on *objects*. None implies any other.

---

# Relate to Other Fields / Compression

**True name:** *faithful = injective-on-arrows, full = surjective-on-arrows, essentially surjective = surjective-on-objects-up-to-iso.* The mnemonic that organizes everything downstream: a fully faithful functor is a **full embedding** — it identifies $\mathcal{C}$ with a full [[Def - Subcategory|subcategory]] of $\mathcal{D}$ — and tacking on essential surjectivity upgrades the embedding to an [[Def - Equivalence of Categories|equivalence]].

The triple mirrors the algebraist's trichotomy for a [[Def - Homomorphism|homomorphism]] $\varphi$: faithful is like injective, full is like "surjective onto the relevant maps", essentially surjective is like surjective on the underlying objects. But there is a categorical twist absent in algebra: because objects are only ever compared up to isomorphism, the object-level condition carries an "essentially", and that single word is responsible for the gap between equivalence and isomorphism of categories.

---

# Examples / Corollaries

**Forgetful functor is faithful, not full.** $U : \mathbf{Grp} \to \mathbf{Set}$ is faithful (distinct homomorphisms have distinct underlying functions) but not full (e.g. for $G = \mathbb{Z}$, most functions $\mathbb{Z} \to \mathbb{Z}$ are not group homomorphisms — only $n \mapsto kn$ are — so $U_{\mathbb{Z},\mathbb{Z}}$ misses them). This is the canonical example separating faithful from full: "concrete but with genuine extra structure".

**Inclusion $\mathbf{Ab} \hookrightarrow \mathbf{Grp}$ is fully faithful.** The inclusion of [[Def - Abelian Group|abelian groups]] into all [[Def - Group|groups]] is faithful (it is injective on objects and morphisms) and full: a group homomorphism between two abelian groups is, of course, a homomorphism, so every arrow downstairs lifts. It is *not* essentially surjective — non-abelian groups like $S_3$ are not isomorphic to any abelian group. So $\mathbf{Ab}$ sits inside $\mathbf{Grp}$ as a full [[Def - Subcategory|subcategory]], the prototype of a fully faithful non-equivalence.

**Fully faithful functors reflect isomorphisms.** If $F$ is fully faithful and $Ff : FA \to FB$ is an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]], then $f$ is an isomorphism. The proof is short and shows the two conditions pulling together: let $h : FB \to FA$ be the inverse of $Ff$. By fullness, $h = Fg$ for some $g : B \to A$. Then $F(g \circ f) = Fg \circ Ff = h \circ Ff = 1_{FA} = F(1_A)$, and by faithfulness $g \circ f = 1_A$; symmetrically $f \circ g = 1_B$. So $f$ is an iso with inverse $g$. This corollary is the engine of [[Thm - Characterization of Equivalence]].

**Is NOT faithful — a constant functor.** The functor $\mathbf{Grp} \to \mathbf{1}$ to the [[Def - Category|terminal category]] sends everything to the unique object and every morphism to the unique identity. It collapses all parallel morphisms together, so it is wildly non-faithful. It *is* full (the only arrow in $\mathbf{1}$ is hit) and essentially surjective, demonstrating that full $+$ essentially surjective without faithful is far from an equivalence.

**Is NOT essentially surjective — $\mathbf{Ab} \hookrightarrow \mathbf{Grp}$.** As above, the fully faithful inclusion fails essential surjectivity. This shows fully faithful alone is an *embedding*, not an equivalence: $\mathcal{C}$ is identified with a part of $\mathcal{D}$, but not all of it.

**Calibration check.** Verify the three properties are logically independent by placing each of the four examples above into the right box. Verify that a fully faithful functor is automatically injective on isomorphism classes of objects (if $FA \cong FB$ then $A \cong B$ — pull the iso back through the hom-bijection and use reflection of isos). Confirm you can state, without looking, the one-line reason fully faithful functors reflect isomorphisms (pull the inverse back by fullness; check it is inverse by faithfulness).

---

# Unlocked by This

> [!tip] The Yoneda Embedding *(from this subject, Chapter II)*
> The [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ is **fully faithful** — that is the entire content of [[Thm - The Yoneda Embedding is Fully Faithful|its theorem]]. Full faithfulness is what makes it an *embedding*: $\mathcal{C}$ lives inside its presheaf category as a full subcategory, and "an object is its hom-functor" becomes literally true.

> [!tip] Reflective Subcategories and Localization *(from this subject, Chapter IV)*
> A **reflective subcategory** is a fully faithful inclusion with a left [[Def - Adjunction|adjoint]] (the reflector). Sheafification, abelianization, and completion are all reflectors onto fully faithful subcategories — the general pattern behind "best approximation by a nicer object".

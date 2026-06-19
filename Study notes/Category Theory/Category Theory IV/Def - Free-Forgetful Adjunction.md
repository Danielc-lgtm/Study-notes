---
type: definition
subject: category-theory
prereqs:
  - "Def - Adjunction"
  - "Def - Unit and Counit of an Adjunction"
  - "Def - Universal Property and Universal Arrow"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{A}$ is a category of "structured sets" (groups, modules, vector spaces, monoids, topological spaces, ...) and $U : \mathcal{A} \to \mathbf{Set}$ is its **forgetful functor**, sending a structured object to its underlying set and a structure-preserving map to the underlying function. A **free functor** is a left adjoint $F : \mathbf{Set} \to \mathcal{A}$ to $U$, so $F \dashv U$ (see [[Def - Adjunction]]). We write $FS$ for the free $\mathcal{A}$-object on a set $S$, $\eta_S : S \to UFS$ for the unit (**insertion of generators**), and $\varepsilon_A : FUA \to A$ for the counit. More generally $U : \mathcal{A} \to \mathcal{B}$ may forget down to a less-structured category $\mathcal{B}$ rather than to $\mathbf{Set}$. The full symbol registry is on [[Category Theory IV — Adjunctions]].

---

# Axiom Motivation

This is less a new definition than the recognition that an entire genre of constructions you already know — the free group, the free module, the free vector space, the polynomial ring, the free monoid, the tensor algebra — are all *the same kind of thing*, and that the thing is one half of an adjunction. The motivation is to extract what they share.

Start from the desideratum. We have a category $\mathcal{A}$ of structured objects and a forgetful functor $U : \mathcal{A} \to \mathbf{Set}$. Given a bare set $S$ of "generators", we want the **most efficient** $\mathcal{A}$-structure built on $S$: efficient meaning *no relations beyond those forced by the axioms of $\mathcal{A}$*. For groups this is the free group, whose elements are reduced words in $S$ and $S^{-1}$ with no accidental coincidences; for vector spaces it is the space $k^{(S)}$ with $S$ as a basis. What does "most efficient" mean precisely? It means: a structure-preserving map *out of* the free object should be as unconstrained as possible — you should be able to send the generators anywhere and have the map exist and be unique. That is exactly a [[Def - Universal Property and Universal Arrow|universal property]]:

> There is a function $\eta_S : S \to UFS$ (insertion of generators) such that for every object $A \in \mathcal{A}$ and every function $g : S \to UA$, there is a *unique* $\mathcal{A}$-morphism $\widehat{g} : FS \to A$ with $U\widehat{g} \circ \eta_S = g$.

Now compress this. The universal property says: morphisms $FS \to A$ in $\mathcal{A}$ are in natural bijection with functions $S \to UA$ in $\mathbf{Set}$, via $\widehat{g} \mapsto U\widehat{g}\circ\eta_S$. But "a natural bijection $\mathcal{A}(FS, A) \cong \mathbf{Set}(S, UA)$" is *precisely* the statement $F \dashv U$. **So a free construction is exactly a left adjoint to a forgetful functor, and its universal arrow is exactly the adjunction's unit.** The free object is not a clever ad-hoc construction; it is the value of the left adjoint, and there is one whenever the forgetful functor has a left adjoint.

Why does the freeness sit on the *left*? Because "maps out of $FS$ are easy" is the defining slogan of a left adjoint ($F$ applied to the source). Forgetful functors land on the *right* because "maps into a forgotten structure are just maps of underlying data" — a map $S \to UA$ is a bare function, the easy thing. This handedness is not a convention; it is forced by which hom-set is the easy one.

What would break if we tried to put the free functor on the right, i.e. as a right adjoint to some functor? Then by [[Thm - Right Adjoints Preserve Limits|RAPL]] it would have to preserve limits — products in particular — and free constructions notoriously do not: the free group on a two-element product is not the product of free groups, because freeness multiplies generators rather than pairing them. Free functors preserve *coproducts* (the free group on a disjoint union is the [[Def - Free Group and Free Product|free product]]), which is the signature of a left adjoint. So the handedness is detectable from the preservation behaviour alone.

A subtler motivation: why insist the forgetful functor go to $\mathbf{Set}$? It need not. The construction is the same whenever $U : \mathcal{A} \to \mathcal{B}$ forgets *some* structure: the abelianisation is left adjoint to $\mathbf{Ab} \hookrightarrow \mathbf{Grp}$ (forget non-commutativity), the free commutative ring on a ring is left adjoint to $\mathbf{CRing} \hookrightarrow \mathbf{Ring}$, the free monoid-completion, and so on. "Free-forgetful" is a *shape* of adjunction — left adjoint to a forgetting — not a statement about sets. The set case is just the most common and the most striking, because the underlying-set functor forgets the most.

---

# The Definition

Let $U : \mathcal{A} \to \mathcal{B}$ be a [[Def - Functor|functor]] (typically a **forgetful functor**, $\mathcal{B} = \mathbf{Set}$). A **free functor** for $U$ is a left adjoint $F : \mathcal{B} \to \mathcal{A}$, so that
$$\mathcal{A}(FS, A) \;\cong\; \mathcal{B}(S, UA) \qquad \text{naturally in } S \in \mathcal{B},\ A \in \mathcal{A}.$$
The adjunction $F \dashv U$ is a **free-forgetful adjunction**. For each $S$, the object $FS$ is the **free $\mathcal{A}$-object on $S$**, and the unit component $\eta_S : S \to UFS$ is the **insertion of generators**; it is the [[Def - Universal Property and Universal Arrow|universal arrow]] from $S$ to $U$:

> For every $A \in \mathcal{A}$ and every morphism $g : S \to UA$ in $\mathcal{B}$, there is a unique morphism $\widehat{g} : FS \to A$ in $\mathcal{A}$ with $U\widehat{g} \circ \eta_S = g$.

The counit component $\varepsilon_A : FUA \to A$ is the unique morphism with $U\varepsilon_A \circ \eta_{UA} = 1_{UA}$; concretely it "evaluates" the free structure on the underlying data of $A$ down into $A$ (multiplies a formal word out, sums a formal linear combination).

---

# Categorical / Structural Definition

The free-forgetful adjunction is the categorical home of the phrase "presented by generators and relations". An object of $\mathcal{A}$ is **free** when it is isomorphic to $FS$ for some $S$; equivalently when the counit $\varepsilon_A : FUA \to A$ admits a section, equivalently when it has a basis on which structure-maps are freely determined. A *general* object of $\mathcal{A}$ is a quotient of a free one: the counit $\varepsilon_A : FUA \to A$ is surjective (in the relevant sense) for every $A$, exhibiting $A$ as the free object on its own underlying set, modulo relations. This is the categorical statement that "every group is a quotient of a free group", "every module is a quotient of a free module", and so on — it is the existence of a *canonical presentation*, and it is the engine of the bar construction and of monadic descent (Chapter V).

Structurally, the composite $T = UF : \mathbf{Set} \to \mathbf{Set}$ is a [[Def - Monad and Comonad|monad]] — the "free $\mathcal{A}$-structure" monad — whose algebras are, under good conditions, exactly the objects of $\mathcal{A}$. This is the precise sense in which "an $\mathcal{A}$-object is a set with operations": it is an algebra for the free-structure monad.

---

# Relate to Other Fields / Compression

Across algebra, the free-forgetful adjunction is the same theorem wearing different clothes. In group theory the free object is the [[Def - Free Group and Free Product|free group]] $FS$ on a set; in module theory it is the [[Def - Free Module|free module]] $R^{(S)}$ over $R$; in linear algebra it is the [[Def - Vector Space|vector space]] $k^{(S)}$ with basis $S$; in ring theory the free commutative ring on $n$ generators is the polynomial ring $k[x_1, \dots, x_n]$; in the theory of monoids the free monoid on $S$ is the set of finite lists ("strings") over $S$ with concatenation. The "underlying set" functor forgets all the structure, and its left adjoint rebuilds the *freest* possible structure. The reason these are identical is that they are all instances of one adjunction-shape; learning the group case once means the rest cost nothing.

**True name:** *the free object is the value of the left adjoint to forgetting, and its universal property IS the adjunction unit.* When you see "the free X on generators $S$", do not picture the explicit construction (words, tuples, lists) — picture the bijection $\mathcal{A}(FS, A) \cong \mathbf{Set}(S, UA)$ and the slogan "a map out of the free object is a free choice of where the generators go". That bijection tells you instantly that the free functor preserves [[Def - Product and Coproduct|coproducts]], that the forgetful functor preserves limits, and that $FS$ is unique up to canonical isomorphism.

---

# Examples / Corollaries

**Is an instance — the free group.** $F : \mathbf{Set} \to \mathbf{Grp}$, with $FS$ the reduced words in $S \sqcup S^{-1}$. The bijection $\mathbf{Grp}(FS, H) \cong \mathbf{Set}(S, UH)$ says a homomorphism is a free choice of generator images. The unit inserts generators; the counit $\varepsilon_H : FUH \to H$ multiplies formal words out. By [[Thm - Right Adjoints Preserve Limits|LAPC]], $F(S \sqcup T) = FS * FT$ ([[Def - Free Group and Free Product|free product]]) — the free functor preserves coproducts.

**Is an instance — the free vector space.** $F : \mathbf{Set} \to \mathbf{Vect}_k$, $FS = k^{(S)}$, the space of finitely-supported functions $S \to k$, with basis $S$. A linear map out of $k^{(S)}$ is a free choice of where to send each basis vector: $\mathbf{Vect}_k(k^{(S)}, V) \cong \mathbf{Set}(S, UV)$. This is the categorical content of "a linear map is determined by its action on a basis, and the basis can go anywhere".

**Is an instance — the free $R$-module and the tensor-hom connection.** $F : \mathbf{Set} \to \mathbf{Mod}_R$, $FS = R^{(S)}$ the [[Def - Free Module|free module]]. Relatedly, *extension of scalars* $- \otimes_R S : \mathbf{Mod}_R \to \mathbf{Mod}_S$ along a ring map $R \to S$ is left adjoint to *restriction of scalars*, another free-forgetful-shaped adjunction; it is "free" in the direction of adding the larger ring's action.

**Is an instance — abelianisation (forgetful to a subcategory).** The inclusion $\mathbf{Ab} \hookrightarrow \mathbf{Grp}$ "forgets" nothing visible but restricts to commutative groups; its left adjoint is the abelianisation $G \mapsto G/[G,G]$. This is a free-forgetful adjunction where the right adjoint is a full inclusion — i.e. a [[Def - Reflective Subcategory|reflective subcategory]]. The free object here is the freest abelian quotient.

**Is NOT an instance — the forgetful functor $\mathbf{Field} \to \mathbf{Set}$ has no free functor.** There is no free field on a set: a left adjoint would have to preserve coproducts and choose a characteristic, and no functorial choice exists. The absence of a left adjoint is exactly the absence of a "free field" — the universal property has no solution.

**Is NOT an instance — a forgetful functor that is itself a left adjoint.** The forgetful functor $\mathbf{Top} \to \mathbf{Set}$ has a left adjoint (discrete topology) *and* a right adjoint (indiscrete topology); the discretization functor is the free one. But the *indiscrete* functor, although adjoint to $U$, is **not** a free-forgetful adjunction in the usual sense — it is a *co*free construction, the right adjoint. Free-forgetful specifically names the left-adjoint-to-forgetting half. (See [[Ex - Discrete and indiscrete topologies as adjoints]].)

**Corollary — every object is canonically presented.** The counit $\varepsilon_A : FUA \to A$ presents each $A$ as a quotient of the free object on its own elements. For groups this recovers "every group is a quotient of a free group".

**Corollary — uniqueness of free objects.** Since $FS$ is a left adjoint value, it is unique up to unique isomorphism by [[Thm - Adjoints are Unique up to Natural Isomorphism]]. So "the" free group is well-defined.

**Calibration check.** State the free-forgetful bijection for monoids and identify the free monoid on $S$ (finite lists over $S$). Verify the unit for vector spaces is "$s \mapsto$ the basis vector $e_s$" and the counit $\varepsilon_V : k^{(UV)} \to V$ is "evaluate the formal linear combination". Explain why the free functor preserves coproducts but not products, citing handedness.

---

# Unlocked by This

> [!tip] Monads and Algebras *(from Chapter V)*
> The composite $UF$ of a free-forgetful adjunction is the prototypical [[Def - Monad and Comonad|monad]], and its **algebras** (Eilenberg–Moore) recover the structured objects: an algebra for the free-group monad is a group, an algebra for the free-vector-space monad is a vector space. This is the **Barr–Beck** circle of ideas — recognising a category as "algebras for a monad" — and it is how Chapter V makes "structure = set with operations" precise.

> [!tip] The Probability Monad and Markov Categories *(from Categorical Probability — Cluster 3)*
> The free-forgetful adjunction between sets and convex spaces (or measurable spaces and their probabilistic algebras) yields the **distribution / Giry monad**, whose Kleisli category is the category of stochastic maps. This is the foundation of **Markov categories** and **categorical probability**, the user's research domain: adjunctions here build the monad in which conditioning and Bayesian inversion become categorical operations.

> [!tip] Presentations, Syntax, and the Free Model *(from Universal Algebra / Logic)*
> "Generators and relations" is the free object modulo the image of a map of free objects. This is how **Lawvere theories** and **algebraic theories** present categories of models, and how the **free CCC** presents the simply typed lambda calculus (Curry-Howard-Lambek). The syntax of a theory is its free model.

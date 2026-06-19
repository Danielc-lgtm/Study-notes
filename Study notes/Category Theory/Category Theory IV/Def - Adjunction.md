---
type: definition
subject: category-theory
prereqs:
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Hom-Functor and Representable Functor"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ and $\mathcal{D}$ are categories and $F : \mathcal{C} \to \mathcal{D}$, $G : \mathcal{D} \to \mathcal{C}$ are [[Def - Functor|functors]]. We write $\mathcal{C}(A, B)$ for the set of morphisms $A \to B$ in $\mathcal{C}$. The turnstile $F \dashv G$ reads "$F$ is **left adjoint** to $G$", equivalently "$G$ is **right adjoint** to $F$". The defining bijection is written $\mathcal{D}(FA, B) \cong \mathcal{C}(A, GB)$, with the left adjoint $F$ always applied to the *source* object $A$ and the right adjoint $G$ to the *target* object $B$. A morphism $f : FA \to B$ and its image $f^{\flat} : A \to GB$ under this bijection are **transposes** or **adjuncts**; the inverse passage sends $g : A \to GB$ to $g^{\sharp} : FA \to B$. The full symbol registry is on [[Category Theory IV — Adjunctions]].

A standing convention: the placement $F : \mathcal{C} \to \mathcal{D}$ for the left adjoint and $G : \mathcal{D} \to \mathcal{C}$ for the right adjoint, with the hom-set bijection reading source-on-the-left, is fixed for the whole chapter. Reversing it inverts every downstream statement.

---

# Axiom Motivation

The right way to arrive at this definition is to notice that the same phrase keeps recurring across mathematics and to ask what it means. "A homomorphism out of the free group on $S$ is the same as a function from $S$." "A bilinear map out of $A \times B$ is the same as a linear map out of $A \otimes B$." "A continuous map from the discretization of $S$ is the same as a function from $S$." "A map of one extra argument is the same as a map valued in functions." Each says: *the morphisms out of one constructed object correspond, naturally and bijectively, to the morphisms into another object built differently.* The definition of an adjunction is the distillation of exactly this phrase.

So suppose we have two functors $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$, and we want to express "maps out of $FA$ are the same as maps into $GB$". The minimal demand is a bijection of sets
$$\Phi_{A,B} : \mathcal{D}(FA, B) \xrightarrow{\ \cong\ } \mathcal{C}(A, GB)$$
for each pair of objects $A \in \mathcal{C}$, $B \in \mathcal{D}$. A bare family of bijections, one per pair, is *not* enough, and seeing why is the heart of the definition. Consider the free-group example with $A = S$ a set and the bijection $\mathbf{Grp}(FS, H) \cong \mathbf{Set}(S, UH)$. If you compose a homomorphism $FS \to H$ with a homomorphism $H \to H'$ on the left, the corresponding function on generators should compose with $U(H \to H')$ on the right — that is, the bijection must commute with postcomposition. Likewise precomposing with a map of generators $S' \to S$ should correspond on the other side. Without these compatibilities the bijection is an accident at each pair and carries no structural content; the constructions $F$ and $G$ would not be linked as *functors* at all, only object-by-object. **The naturality requirement is precisely what upgrades a coincidence of cardinalities into a relationship between functors.**

What breaks if we drop naturality and keep only the family of bijections? Everything that makes adjunctions useful. The unit and counit (the next definition) are *built* from the bijection by transposing identity morphisms, and their assembly into natural transformations relies on naturality of $\Phi$. The theorem that right adjoints preserve limits relies on naturality, because the proof commutes the bijection past the limit cone's legs. Drop naturality and you keep a curiosity — $|\mathcal{D}(FA,B)| = |\mathcal{C}(A,GB)|$ — and lose every theorem. As a concrete failure, on finite sets and finite groups one can rig isolated bijections of hom-sets that respect no maps; they are useless.

Why a bijection and not merely an injection, or a natural transformation $\mathcal{D}(F-,-) \to \mathcal{C}(-,G-)$ that need not be invertible? Because the content is *equality* of the two notions of morphism: a map out of $F$ must be exactly, recoverably, a map into $G$. A natural transformation in one direction only is a weaker and genuinely different notion (it appears in the theory of "relative adjunctions" and of Kan extensions), and it does not give a unit-counit pair satisfying the triangle identities. The invertibility is what lets you transpose *both ways* and is what the triangle identities encode. If you strengthen the requirement instead — demand that $F$ and $G$ be mutually inverse equivalences, $FG \cong 1$ and $GF \cong 1$ — you collapse to the much rarer notion of an [[Def - Equivalence of Categories|equivalence of categories]], which is an adjunction whose unit and counit are *isomorphisms*. Adjunction is the Goldilocks notion: a two-way bijection of hom-sets, natural, but with no demand that the composites $FG$, $GF$ be the identity.

One more design question: why state it with $F$ on the source and $G$ on the target, rather than symmetrically? Because the asymmetry is the point. The left adjoint is a "free, generated, colimit-like" construction and the right adjoint is a "cofree, limit-like" construction, and the convention $\mathcal{D}(FA, B) \cong \mathcal{C}(A, GB)$ places each on the side where it does its work. The same two functors are essentially never adjoint in both directions at once (that would again force an equivalence); the handedness is real structure, not a labelling choice.

---

# The Definition

Let $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ be [[Def - Functor|functors]]. An **adjunction** from $F$ to $G$, written $F \dashv G$, is a family of bijections
$$\Phi_{A,B} : \mathcal{D}(FA, B) \xrightarrow{\ \cong\ } \mathcal{C}(A, GB) \qquad (A \in \mathcal{C},\ B \in \mathcal{D})$$
that is **natural in both $A$ and $B$**. Naturality means: for every $f : FA \to B$, every morphism $h : A' \to A$ in $\mathcal{C}$, and every morphism $k : B \to B'$ in $\mathcal{D}$,
$$\Phi_{A',B'}\big(k \circ f \circ Fh\big) \;=\; Gk \circ \Phi_{A,B}(f) \circ h.$$
Equivalently, the two bifunctors $\mathcal{C}^{op} \times \mathcal{D} \to \mathbf{Set}$ given by $(A, B) \mapsto \mathcal{D}(FA, B)$ and $(A, B) \mapsto \mathcal{C}(A, GB)$ are naturally isomorphic.

$F$ is called the **left adjoint** and $G$ the **right adjoint**. For $f : FA \to B$, the morphism $\Phi(f) : A \to GB$ is its **transpose** (or **adjunct**); for $g : A \to GB$, the morphism $\Phi^{-1}(g) : FA \to B$ is its transpose. Transposition is a mutually inverse pair of operations.

The naturality condition unpacks into two halves, which it is worth stating separately because proofs use them one at a time:

1. **Naturality in $B$ (postcomposition).** For $f : FA \to B$ and $k : B \to B'$, $\quad \Phi(k \circ f) = Gk \circ \Phi(f)$.
2. **Naturality in $A$ (precomposition).** For $f : FA \to B$ and $h : A' \to A$, $\quad \Phi(f \circ Fh) = \Phi(f) \circ h$.

---

# Categorical / Structural Definition

The hom-set definition above *is* the categorical definition; an adjunction is a relationship internal to category theory and has no "underlying set" reformulation. But there are two further structural repackagings, both proved equivalent in [[Thm - Equivalence of the Definitions of Adjunction]], and each is the natural definition for a different purpose.

**Via unit and counit.** An adjunction $F \dashv G$ is equivalently a pair of [[Def - Natural Transformation|natural transformations]], the **unit** $\eta : 1_{\mathcal{C}} \Rightarrow GF$ and the **counit** $\varepsilon : FG \Rightarrow 1_{\mathcal{D}}$, satisfying the two **triangle identities** $(\varepsilon F) \circ (F\eta) = 1_F$ and $(G\varepsilon) \circ (\eta G) = 1_G$. The transpose of $f : FA \to B$ is recovered as $Gf \circ \eta_A$, and the transpose of $g : A \to GB$ as $\varepsilon_B \circ Fg$. This is the form that survives into [[Def - Monad and Comonad|monad]] theory and into $2$-categorical reasoning. See [[Def - Unit and Counit of an Adjunction]].

**Via universal arrows / representability.** Fixing $A \in \mathcal{C}$, the bijection $\mathcal{D}(FA, -) \cong \mathcal{C}(A, G-)$ says the object $FA$ **represents** the functor $\mathcal{C}(A, G-) : \mathcal{D} \to \mathbf{Set}$, with representing element the unit $\eta_A : A \to GFA$. Thus $G$ has a left adjoint *if and only if* the functor $\mathcal{C}(A, G-)$ is [[Def - Hom-Functor and Representable Functor|representable]] for every $A$, and the left adjoint sends $A$ to its representing object. Dually $\eta_A$ is a **universal arrow** from $A$ to $G$: an [[Def - Initial and Terminal Object|initial object]] of the comma category $(A \downarrow G)$ whose objects are pairs $(B, A \xrightarrow{} GB)$. This is the form that connects adjunctions to the [[Def - Universal Property and Universal Arrow|universal properties]] of Chapter II.

---

# Relate to Other Fields / Compression

An adjunction is the categorical generalisation of a **Galois connection** between posets. If $P$ and $Q$ are partially ordered sets viewed as categories (one morphism $a \to b$ exactly when $a \leq b$), then a pair of monotone maps $f : P \to Q$, $g : Q \to P$ is an adjunction $f \dashv g$ exactly when $f(a) \leq b \iff a \leq g(b)$ for all $a, b$ — which is the standard definition of a (monotone) Galois connection. The hom-set bijection degenerates to a bi-implication because hom-sets in a poset have at most one element. Closure operators, the Galois correspondence of field theory, and order-theoretic completions are all instances; adjunctions are "Galois connections with witnesses".

An adjunction is also the precise sense in which one operation is **the best approximation** to inverting another. The free functor does not invert forgetting (you cannot recover a group from its underlying set), but it is the universal attempt: the unit $\eta$ measures the gap. This is the same idea as a left/right inverse in linear algebra, a pseudo-inverse, or a projection onto a subspace — an adjoint is a "one-sided inverse up to a universal arrow".

**True name:** *an adjunction is the statement "maps out of $F$ equal maps into $G$", naturally.* The official definition is the natural bijection $\mathcal{D}(FA, B) \cong \mathcal{C}(A, GB)$; the operational name you reach for is the slogan, because it tells you instantly which functor is on the left (the one applied to sources, the one building free structure) and which transpose to compute on which side.

---

# Examples / Corollaries

**Is an instance — free $\dashv$ forgetful for groups.** Let $U : \mathbf{Grp} \to \mathbf{Set}$ forget the group structure and $F : \mathbf{Set} \to \mathbf{Grp}$ form the [[Def - Free Group and Free Product|free group]]. Then $F \dashv U$, witnessed by $\mathbf{Grp}(FS, H) \cong \mathbf{Set}(S, UH)$: a homomorphism out of the free group is determined by, and may freely choose, the images of the generators. The unit $\eta_S : S \to UFS$ inserts the generators; the counit $\varepsilon_H : FUH \to H$ multiplies a formal word out into a genuine product. The same pattern gives free $\dashv$ forgetful for the [[Def - Free Module|free $R$-module]] over $\mathbf{Mod}_R$ and the free [[Def - Vector Space|vector space]] over $\mathbf{Vect}_k$.

**Is an instance — the tensor-hom adjunction.** Fix a [[Def - Module|module]] $M$ over a ring $R$. The functor $- \otimes_R M$ is left adjoint to $\mathrm{Hom}_R(M, -)$:
$$\mathrm{Hom}_R(A \otimes_R M, B) \;\cong\; \mathrm{Hom}_R(A, \mathrm{Hom}_R(M, B)).$$
A map out of the [[Def - Tensor Product of Modules|tensor product]] $A \otimes_R M$ is a bilinear map on $A \times M$ (this is the [[Thm - Universal Property of the Tensor Product of Modules|universal property of the tensor product]]), and a bilinear map is the same as a linear map $A \to \mathrm{Hom}_R(M, B)$ sending each $a$ to the map $m \mapsto$ (its bilinear pairing). This is "currying" for modules, and it is why $\otimes$ is right exact while [[Def - The Hom Functor and Left Exactness|$\mathrm{Hom}$]] is left exact — left adjoints preserve colimits, right adjoints preserve limits.

**Is an instance — the chain $\coprod \dashv \Delta \dashv \prod$.** Let $\Delta : \mathcal{C} \to \mathcal{C} \times \mathcal{C}$ be the diagonal functor $A \mapsto (A, A)$. Its left adjoint is the [[Def - Product and Coproduct|coproduct]] $(X, Y) \mapsto X \sqcup Y$ and its right adjoint is the product $(X, Y) \mapsto X \times Y$, because $\mathcal{C}(X \sqcup Y, A) \cong \mathcal{C}(X, A) \times \mathcal{C}(Y, A) = (\mathcal{C}\times\mathcal{C})((X,Y), \Delta A)$ and dually $(\mathcal{C}\times\mathcal{C})(\Delta A, (X,Y)) \cong \mathcal{C}(A, X \times Y)$. So the product and coproduct are *themselves* adjoints to the diagonal — the cleanest illustration that a left adjoint is colimit-like and a right adjoint limit-like.

**Is NOT an instance — a pair of functors with isolated hom-set bijections that are not natural.** Take $\mathcal{C} = \mathcal{D} = \mathbf{FinSet}$, and let $F = G = \mathrm{id}$. The hom-sets $\mathbf{FinSet}(A, B)$ and $\mathbf{FinSet}(A, B)$ are literally equal, so they are in bijection by the identity — and the identity *is* natural, giving the trivial adjunction $\mathrm{id} \dashv \mathrm{id}$. But now choose, for each pair $(A, B)$ of sets, an *arbitrary* bijection of the finite set $\mathbf{FinSet}(A, B)$ with itself (a permutation of the function set). Each $\Phi_{A,B}$ is still a bijection of hom-sets of the right shape, but a generic choice fails naturality — it does not commute with composition — so it is **not** an adjunction. This is the canonical witness that a bijection of hom-sets at each pair is far weaker than an adjunction; naturality is the whole content.

**Is NOT an instance — the forgetful functor $\mathbf{Field} \to \mathbf{Set}$ has no left adjoint.** There is no "free field on a set". If a left adjoint $F$ existed, by [[Thm - Right Adjoints Preserve Limits|RAPL/LAPC]] it would preserve coproducts, but there is no field generated freely by a set in a way compatible with field homomorphisms (fields have no coproducts in general, and the would-be free field would have to choose a characteristic). The non-existence is detected exactly by a failure of the adjoint's required preservation property.

**Corollary — transposition is involutive.** $\Phi^{-1}(\Phi(f)) = f$ and $\Phi(\Phi^{-1}(g)) = g$. Equivalently, "transposing twice is the identity": this is just that $\Phi$ is a bijection, but it is the workhorse identity in every adjunction computation.

**Corollary — the adjunction determines $F$ from $G$ (and vice versa) up to isomorphism.** Since $FA$ represents $\mathcal{C}(A, G-)$, and representing objects are unique up to unique isomorphism, the left adjoint is determined by the right adjoint. See [[Thm - Adjoints are Unique up to Natural Isomorphism]].

**Calibration check.** Verify that $\mathrm{id} \dashv \mathrm{id}$ for any category (the trivial adjunction). Check that the two halves of naturality (postcomposition by $k$, precomposition by $Fh$) are independent statements by writing each as a commuting square in $\mathbf{Set}$. And confirm, on the free-group example, that the transpose of the identity homomorphism $1_{FS} : FS \to FS$ is exactly the insertion of generators $S \to UFS$ — this is the computation that defines the unit.

---

# Unlocked by This

> [!tip] Unit, Counit, and Monads *(from this chapter and Chapter V)*
> The transposes of identity morphisms are the **unit** and **counit**; assembling them gives the $2$-categorical face of the adjunction (see [[Def - Unit and Counit of an Adjunction]]). Composing $GF$ then produces a **monad**, the structure Chapter V is built on — every adjunction generates one.

> [!tip] Internal Hom and Closed Monoidal Categories *(from Monoidal Category Theory)*
> When the adjunction is $- \otimes B \dashv [B, -]$ for a monoidal product $\otimes$, the right adjoint $[B,-]$ is the **internal hom**, and the category is **closed monoidal**. The [[Def - Cartesian Closed Category|cartesian closed]] case ($\otimes = \times$) is the model of typed lambda calculus; the general case underlies **enriched category theory** and the symmetric monoidal categories of **categorical probability** and **TQFT**.

> [!tip] Geometric Morphisms and Topoi *(from Topos Theory)*
> A **geometric morphism** of topoi is an adjunction $f^* \dashv f_*$ whose left adjoint $f^*$ preserves finite limits. The entire theory of **topoi** as "generalized spaces" is organized around such adjunctions; the inclusion of sheaves into presheaves as a reflective subcategory (with sheafification the reflector) is the prototype.

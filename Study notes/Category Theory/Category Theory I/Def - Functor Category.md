---
type: definition
subject: category-theory
prereqs:
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Category"
tags: [category-theory, foundations]
---

# Notation

For [[Def - Category|categories]] $\mathcal{C}, \mathcal{D}$, the **functor category** is written $[\mathcal{C}, \mathcal{D}]$ or $\mathcal{D}^{\mathcal{C}}$ or $\mathbf{Fun}(\mathcal{C}, \mathcal{D})$. Its objects are [[Def - Functor|functors]] $F, G : \mathcal{C} \to \mathcal{D}$ and its morphisms are [[Def - Natural Transformation|natural transformations]] $\alpha : F \Rightarrow G$. Vertical composition of $\alpha : F \Rightarrow G$ and $\beta : G \Rightarrow H$ is $\beta \cdot \alpha$ or just $\beta \circ \alpha$; horizontal composition (whiskering) is written $\beta \ast \alpha$. A **presheaf category** is $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

We now have three layers — objects, [[Def - Functor|functors]], [[Def - Natural Transformation|natural transformations]] — and the natural question is whether the top two layers themselves form a [[Def - Category|category]]. They do, and recognizing this is not a triviality: it is the observation that unlocks half of advanced category theory. The functors $\mathcal{C} \to \mathcal{D}$ are the objects, the natural transformations between them are the morphisms, and we only need to check that natural transformations compose associatively and have identities. They do — *componentwise* — because composition and identities in $[\mathcal{C}, \mathcal{D}]$ are inherited from $\mathcal{D}$ at each object.

The motivation for caring is that **the most important categories in mathematics are functor categories**. A [[Def - Group|group]] representation is a functor $\mathbf{B}G \to \mathbf{Vect}_k$, so the category of representations is a functor category $[\mathbf{B}G, \mathbf{Vect}_k]$ — and its morphisms, the natural transformations, are exactly the intertwiners (the $G$-equivariant maps). A presheaf is a functor $\mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$, so all of sheaf theory and a great deal of algebraic geometry lives in functor categories $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$. A diagram of shape $\mathcal{J}$ is a functor $\mathcal{J} \to \mathcal{C}$, so the category of $\mathcal{J}$-shaped diagrams — where limits and colimits are computed — is the functor category $[\mathcal{J}, \mathcal{C}]$. The single construction $[\mathcal{C}, \mathcal{D}]$ subsumes all of these.

Why is vertical composition the right notion of composing morphisms here, and not some other? Because a morphism in $[\mathcal{C}, \mathcal{D}]$ should be a transformation, and transformations compose by composing components: $(\beta \circ \alpha)_A = \beta_A \circ \alpha_A$. **Drop componentwise composition** and there is no other associative, unital choice that uses the naturality squares — the naturality square of the composite is the vertical pasting of the two given squares, which commutes automatically. The identity natural transformation $1_F$ has components $1_{FA}$. With these, the category axioms for $[\mathcal{C}, \mathcal{D}]$ reduce to the category axioms for $\mathcal{D}$, checked one object at a time.

---

# The Definition

Let $\mathcal{C}, \mathcal{D}$ be [[Def - Category|categories]]. The **functor category** $[\mathcal{C}, \mathcal{D}]$ (also $\mathcal{D}^{\mathcal{C}}$) is the category with:

- **objects**: all [[Def - Functor|functors]] $F : \mathcal{C} \to \mathcal{D}$;
- **morphisms** $F \to G$: all [[Def - Natural Transformation|natural transformations]] $\alpha : F \Rightarrow G$;
- **composition**: vertical composition, $(\beta \circ \alpha)_A = \beta_A \circ \alpha_A$;
- **identities**: $(1_F)_A = 1_{FA}$.

The category axioms hold because they hold componentwise in $\mathcal{D}$. When $\mathcal{C}$ is small and $\mathcal{D}$ is locally small, $[\mathcal{C}, \mathcal{D}]$ is locally small. An **isomorphism in $[\mathcal{C}, \mathcal{D}]$** is exactly a [[Def - Natural Transformation|natural isomorphism]].

A **presheaf category** on $\mathcal{C}$ is the functor category $\widehat{\mathcal{C}} := [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$.

---

# Categorical / Structural Definition

The existence of functor categories means $\mathbf{Cat}$, the [[Def - Category|category]] of small categories and functors, is not merely a category but a **2-category**: between any two objects $\mathcal{C}, \mathcal{D}$ (which are categories) there sits not just a *set* of morphisms but a whole *category* of them, namely $[\mathcal{C}, \mathcal{D}]$. The data of a 2-category is:

- **0-cells**: objects (here, categories);
- **1-cells**: morphisms (here, functors), composed associatively;
- **2-cells**: morphisms between morphisms (here, natural transformations).

The 2-cells admit **two** compositions. **Vertical composition** $\beta \circ \alpha$ composes $\alpha : F \Rightarrow G$ with $\beta : G \Rightarrow H$ (same source and target categories) — this is the composition inside each hom-category $[\mathcal{C}, \mathcal{D}]$. **Horizontal composition** $\beta \ast \alpha$ composes along functor composition: given $\alpha : F \Rightarrow F'$ between $\mathcal{C} \rightrightarrows \mathcal{D}$ and $\beta : G \Rightarrow G'$ between $\mathcal{D} \rightrightarrows \mathcal{E}$, it produces $\beta \ast \alpha : G F \Rightarrow G' F'$. **Whiskering** is the special case where one of the two transformations is an identity: $G \alpha : G F \Rightarrow G F'$ (whiskering $\alpha$ by the functor $G$ on the left, components $G(\alpha_A)$) and $\beta F : G F \Rightarrow G' F$ (whiskering $\beta$ by $F$ on the right, components $\beta_{FA}$).

The two compositions are tied together by the **interchange law**: for vertically composable $\alpha, \alpha'$ and $\beta, \beta'$,
$$(\beta' \circ \beta) \ast (\alpha' \circ \alpha) = (\beta' \ast \alpha') \circ (\beta \ast \alpha).$$
In words, a grid of natural transformations can be assembled either by first composing rows then columns, or first columns then rows, with the same result. The interchange law is the coherence condition that makes $\mathbf{Cat}$ a genuine 2-category and is the prototype of all higher-categorical coherence (it is proved in full on [[Thm - The Interchange Law]] in Chapter VII).

---

# Relate to Other Fields / Compression

**True name:** *the category whose points are functors and whose paths are natural transformations* — equivalently, the internal hom $\mathcal{D}^{\mathcal{C}}$ in $\mathbf{Cat}$. The exponential notation $\mathcal{D}^{\mathcal{C}}$ is not decorative: $\mathbf{Cat}$ is [[Def - Cartesian Closed Category|cartesian closed]], and $\mathcal{D}^{\mathcal{C}}$ is the exponential object, satisfying $\mathbf{Cat}(\mathcal{E} \times \mathcal{C}, \mathcal{D}) \cong \mathbf{Cat}(\mathcal{E}, \mathcal{D}^{\mathcal{C}})$ — the currying isomorphism. This is the same adjunction that, in $\mathbf{Set}$, makes the set of functions $Y^X$ an exponential, and it is why a natural transformation could be packaged as a single functor $\mathcal{C} \times \mathbf{2} \to \mathcal{D}$.

The compression worth carrying: **whenever a kind of mathematical object is "a structure varying over an index category", it is an object of a functor category.** Representations vary over $\mathbf{B}G$; presheaves vary over $\mathcal{C}^{\mathrm{op}}$; diagrams vary over a shape $\mathcal{J}$; chain complexes vary over the poset of integers. The morphisms in the functor category are automatically the "structure-preserving maps of varying objects", which always turn out to be the right notion (intertwiners, sheaf maps, cones, chain maps).

---

# Examples / Corollaries

**Representations of a [[Def - Group|group]].** $[\mathbf{B}G, \mathbf{Vect}_k]$ is the category of $k$-linear [[Def - Group|group]] representations of $G$: an object is a functor $\mathbf{B}G \to \mathbf{Vect}_k$, i.e. a vector space with a $G$-action, and a morphism is a natural transformation, which works out to be exactly a $G$-equivariant linear map (an intertwiner). The naturality square is the equivariance condition $\rho'(g) \circ \alpha = \alpha \circ \rho(g)$.

**Presheaves.** $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ is the presheaf category. When $\mathcal{C}$ is the poset of open sets of a [[Def - Topological Space|space]] (ordered by inclusion), a presheaf is the familiar "assign data to each open set, with restriction maps" — the starting point for **sheaves**. The morphisms are natural transformations, i.e. families of maps commuting with restriction.

**Diagram categories.** $[\mathbf{2}, \mathcal{C}]$, with $\mathbf{2}$ the [[Def - Category|walking arrow]], is the **arrow category** of $\mathcal{C}$: its objects are morphisms of $\mathcal{C}$, its morphisms are commuting squares. More generally $[\mathcal{J}, \mathcal{C}]$ is where $\mathcal{J}$-shaped diagrams live, and [[Def - Limit and Colimit|limits and colimits]] are right and left adjoints to the constant-diagram functor $\mathcal{C} \to [\mathcal{J}, \mathcal{C}]$.

**Is NOT a hom-set of a 1-category.** The "morphisms" between two categories do not form a mere set — they form a category, with its own morphisms (the natural transformations). Forgetting the natural transformations and keeping only functors gives the 1-category $\mathbf{Cat}$, but this *loses information*: two functors can be non-equal yet naturally isomorphic, a distinction invisible in the 1-category. This is the precise sense in which $\mathbf{Cat}$ "wants to be" a 2-category — the 2-cells are real data, not bookkeeping.

**Calibration check.** Verify that an isomorphism in $[\mathcal{C}, \mathcal{D}]$ is a natural isomorphism (a natural transformation invertible in the functor category has componentwise inverses, which are automatically natural). Verify the identity natural transformation $1_F$ is a two-sided identity for vertical composition. Confirm you can write down, for the arrow category $[\mathbf{2}, \mathcal{C}]$, what an object and a morphism are (an object is an arrow of $\mathcal{C}$; a morphism is a commuting square).

---

# Unlocked by This

> [!tip] The Yoneda Embedding and Presheaf Categories *(from this subject, Chapter II)*
> The presheaf category $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ is the home of the [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$, which is fully faithful. Presheaf categories are the **free cocompletion** of $\mathcal{C}$ — the universal way to adjoin all colimits — and every presheaf is a colimit of representables. This is the gateway to topos theory.

> [!tip] 2-Categories, Bicategories, and Higher Category Theory *(from this subject, Chapter VII)*
> $\mathbf{Cat}$ as a 2-category, with whiskering and the [[Thm - The Interchange Law|interchange law]], is the first **2-category**. Weakening associativity and unit laws to hold only up to coherent isomorphism gives **bicategories**; iterating the "morphisms between morphisms" idea gives **∞-categories**, modelled by quasi-categories. Functor categories are the seed of the entire higher-categorical program.

> [!tip] Functor Categories are Cartesian Closed *(from Logic and Type Theory)*
> When $\mathcal{D}$ is [[Def - Cartesian Closed Category|cartesian closed]] (or a topos), so is $[\mathcal{C}, \mathcal{D}]$, computed pointwise. This makes presheaf categories models of higher-order intuitionistic logic and connects to **homotopy type theory** through the Curry–Howard–Lambek correspondence.

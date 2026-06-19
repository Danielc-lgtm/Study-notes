---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Functor Category"
  - "Def - Opposite Category and Duality"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a small category, $\mathcal{C}^{op}$ its [[Def - Opposite Category and Duality|opposite]]. A presheaf is written $F, G, P, X$; its action on objects $F(c)$ and on a morphism $f : c \to d$ in $\mathcal{C}$ is $F(f) : F(d) \to F(c)$ (note the reversal — $F$ is contravariant on $\mathcal{C}$). The **presheaf category** is denoted $[\mathcal{C}^{op}, \mathbf{Set}]$ or $\mathbf{Set}^{\mathcal{C}^{op}}$ or $\mathrm{PSh}(\mathcal{C})$, all synonyms. For a presheaf on a topological space we write $\mathcal{O}(X)$ for the poset of open sets and $\rho^U_V : F(U) \to F(V)$ for restriction along $V \subseteq U$. The full registry is on [[Category Theory II — Universal Properties, Representability, and the Yoneda Lemma]].

---

# Axiom Motivation

A presheaf is the answer to a recurring need: how do you attach data to the objects of a category in a way that is compatible with the morphisms, *contravariantly* — so that a morphism lets you *pull back* or *restrict* data rather than push it forward? The word "presheaf" comes from sheaf theory, where the data is "functions on open sets" and the morphisms are inclusions of open sets, along which functions restrict. But the abstraction strips that down to its skeleton, and the skeleton is just: a contravariant functor to $\mathbf{Set}$.

Why contravariance specifically? Because the motivating examples all *restrict*. If $V \subseteq U$ are open sets in a space and $s$ is a function defined on $U$, you can restrict $s$ to $V$ — data flows from the bigger set to the smaller, against the inclusion $V \hookrightarrow U$. If $f : G \to H$ is a group homomorphism and you have a representation of $H$, you can pull it back to a representation of $G$ — again against the arrow. This "against the arrow" behaviour is exactly contravariance, and it is so pervasive that it deserves its own name and its own ambient category.

The second motivating decision is to *collect all presheaves on $\mathcal{C}$ into one category*, $[\mathcal{C}^{op}, \mathbf{Set}]$, with [[Def - Natural Transformation|natural transformations]] as the morphisms. This is not idle bookkeeping. The presheaf category is extraordinarily well-behaved — it has all [[Def - Limit and Colimit|limits and colimits]], computed pointwise, it is cartesian closed, and crucially the [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$ embeds the original $\mathcal{C}$ into it as a full subcategory. So the presheaf category is the *free cocompletion* of $\mathcal{C}$: the smallest nice category containing $\mathcal{C}$ in which one can freely take colimits. Whenever a construction in $\mathcal{C}$ is awkward because $\mathcal{C}$ lacks the colimits to support it, the standard repair is to embed $\mathcal{C}$ into its presheaves, work there, and recognize the answer. That is why this single definition opens the door to sheaves, schemes, simplicial sets, and topos theory.

One could imagine instead defining a "copresheaf" as a *covariant* functor $\mathcal{C} \to \mathbf{Set}$, and indeed those are studied. But the contravariant version is the canonical one because of the Yoneda embedding: $\mathbf{y}(A) = \mathcal{C}(-, A)$ is contravariant, so the representable functors — the objects of $\mathcal{C}$ as seen inside the functor world — live naturally among presheaves, not copresheaves. The presheaf category is the home of the Yoneda embedding.

---

# The Definition

Let $\mathcal{C}$ be a small category.

A **presheaf** on $\mathcal{C}$ is a contravariant functor
$$F : \mathcal{C}^{op} \to \mathbf{Set}.$$
Explicitly, $F$ assigns to each object $c \in \mathcal{C}$ a set $F(c)$, and to each morphism $f : c \to d$ in $\mathcal{C}$ a function $F(f) : F(d) \to F(c)$ (the direction reverses), such that $F(1_c) = 1_{F(c)}$ and $F(g \circ f) = F(f) \circ F(g)$.

The **presheaf category** $[\mathcal{C}^{op}, \mathbf{Set}]$ (equivalently $\mathbf{Set}^{\mathcal{C}^{op}}$) is the [[Def - Functor Category|functor category]] whose objects are presheaves on $\mathcal{C}$ and whose morphisms are [[Def - Natural Transformation|natural transformations]] between them. A natural transformation $\alpha : F \Rightarrow G$ is a family of functions $\alpha_c : F(c) \to G(c)$, one per object, commuting with all the restriction maps: $\alpha_c \circ F(f) = G(f) \circ \alpha_d$ for every $f : c \to d$.

---

# Categorical / Structural Definition

A presheaf is precisely an object of the functor category $[\mathcal{C}^{op}, \mathbf{Set}]$, so all the structure is inherited from general functor-category theory. Two structural facts are worth stating because they are used constantly:

First, **limits and colimits in $[\mathcal{C}^{op}, \mathbf{Set}]$ are computed pointwise**: $(\lim_i F_i)(c) = \lim_i (F_i(c))$ and likewise for colimits, with the limit/colimit taken in $\mathbf{Set}$ at each object $c$. Because $\mathbf{Set}$ is complete and cocomplete, so is every presheaf category.

Second, **the representable presheaves are the image of the [[Def - The Yoneda Embedding|Yoneda embedding]]** $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$, $A \mapsto \mathcal{C}(-, A)$. By [[Thm - The Yoneda Embedding is Fully Faithful]] this is a full embedding, so $\mathcal{C}$ sits inside its presheaf category as a full subcategory, and a presheaf is [[Def - Hom-Functor and Representable Functor|representable]] exactly when it is isomorphic to one of these. Every presheaf is canonically a colimit of representable presheaves (the *density theorem* / "co-Yoneda lemma"), which is the precise sense in which $[\mathcal{C}^{op}, \mathbf{Set}]$ is generated by $\mathcal{C}$.

---

# Relate to Other Fields / Compression

A presheaf is "$\mathbf{Set}$-valued data that restricts along the morphisms of $\mathcal{C}$". The compression worth carrying is that **a presheaf is a generalized space probed by the objects of $\mathcal{C}$**: think of $F(c)$ as "the set of ways the test-object $c$ maps into the generalized space $F$". Under the Yoneda embedding an honest object $A$ becomes the presheaf $X \mapsto \mathcal{C}(X, A)$, whose value at $X$ is literally "maps from $X$ into $A$" — so presheaves are the natural habitat into which $\mathcal{C}$ generalizes, and many constructions that fail in $\mathcal{C}$ for lack of colimits succeed in $[\mathcal{C}^{op}, \mathbf{Set}]$.

**True name:** a presheaf is *contravariant set-valued data with restriction maps*. When you meet "data on objects that pulls back along morphisms" — sections over opens, coefficients of a cohomology theory before sheafifying, the $n$-simplices of a simplicial object — you are looking at a presheaf, and the presheaf category is where it lives.

---

# Examples / Corollaries

**Is an instance — every representable functor.** For any $A \in \mathcal{C}$, the contravariant hom-functor $\mathcal{C}(-, A) : \mathcal{C}^{op} \to \mathbf{Set}$ is a presheaf, the *representable presheaf* associated to $A$. These are the building blocks: by the density theorem every presheaf is a colimit of representables.

> [!note]- Algebraic geometry / topology background: a presheaf of sets on a space
> No prior sheaf theory is assumed. Let $X$ be a topological space (see [[Def - Topological Space]]). Its open sets, ordered by inclusion, form a poset $\mathcal{O}(X)$, hence a category: there is one morphism $V \to U$ exactly when $V \subseteq U$. A **presheaf of sets on $X$** is, in the classical language of geometry, an assignment $F$ giving to each open set $U$ a set $F(U)$ — think "the set of continuous real-valued functions on $U$", or "the set of sections of some bundle over $U$" — together with, for each inclusion $V \subseteq U$, a **restriction map** $\rho^U_V : F(U) \to F(V)$, such that $\rho^U_U = \mathrm{id}$ and $\rho^V_W \circ \rho^U_V = \rho^U_W$ (restricting in two steps equals restricting in one). Elements of $F(U)$ are called **sections over $U$**.
>
> Now read this categorically. The restriction map goes from the bigger open $U$ to the smaller $V$ — *against* the inclusion morphism $V \to U$ in $\mathcal{O}(X)$. The compatibility conditions are exactly functoriality. So a classical presheaf of sets on a space is precisely a contravariant functor
> $$F : \mathcal{O}(X)^{op} \to \mathbf{Set},$$
> that is, a presheaf on the category $\mathcal{O}(X)$ in the sense of this page. The geometric notion is a *special case* of the categorical one, recovered by taking $\mathcal{C} = \mathcal{O}(X)$. This is illuminating because it shows the categorical definition is not an empty generalization: it is the common skeleton of "data restricting along inclusions" (geometry) and "natural set-valued operations" (the rest of category theory). A **sheaf** is a presheaf satisfying an additional *gluing* axiom — local sections that agree on overlaps glue to a unique global section — and **sheafification** (turning a presheaf into the closest sheaf) is a reflective localization, a left adjoint to the inclusion of sheaves into presheaves (see [[Def - Reflective Subcategory]]). The whole edifice of **schemes**, **Zariski topology**, and cohomology is built on presheaves and sheaves of sets and of rings on a space.

**Is an instance — a simplicial set.** Let $\Delta$ be the **simplex category**: objects are the finite nonempty ordinals $[n] = \{0 < 1 < \cdots < n\}$, morphisms are order-preserving functions. A **simplicial set** is a presheaf on $\Delta$, i.e. a functor $\Delta^{op} \to \mathbf{Set}$. The value at $[n]$ is "the set of $n$-simplices", and the morphisms of $\Delta$ give face and degeneracy maps (restriction in the presheaf sense). Simplicial sets are the combinatorial model of spaces and the foundation of the model-category and $\infty$-category machinery developed in later chapters (forward ref: **simplicial set**, treated fully in Chapter VII).

**Is an instance — a $G$-set as a presheaf on a one-object groupoid.** A group $G$ is a one-object category $BG$; a presheaf $BG^{op} \to \mathbf{Set}$ is a set with a right $G$-action (a right $G$-set). The restriction maps are the action of group elements. This is the example that makes the Yoneda-equals-Cayley story (see [[Ex - Yoneda generalizes Cayley's theorem]]) work.

**Is NOT an instance — a covariant functor $\mathcal{C} \to \mathbf{Set}$.** A covariant set-valued functor is a *copresheaf*, not a presheaf; the variance is the whole distinction. The forgetful functor $\mathbf{Grp} \to \mathbf{Set}$ is a copresheaf. Calling it a presheaf would invert all the restriction maps and break functoriality. (It *is* a presheaf on $\mathbf{Grp}^{op}$, which is a different — and rarely used — statement.)

**Calibration check.** Confirm that for the poset $\mathcal{O}(X)$ the functoriality axiom $F(g \circ f) = F(f) \circ F(g)$ specializes to the two-step restriction rule $\rho^V_W \circ \rho^U_V = \rho^U_W$. Verify that the representable presheaf $\mathcal{O}(X)(-, U)$ assigns to each open $V$ a set with one element if $V \subseteq U$ and none otherwise — and that a natural transformation into a presheaf $F$ out of it is, by Yoneda, just an element of $F(U)$.

---

# Unlocked by This

> [!tip] The Yoneda Embedding *(from this chapter)*
> The presheaf category is the target of the [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$. The [[Thm - The Yoneda Lemma|Yoneda lemma]] is the statement that natural transformations *out of* a representable presheaf $\mathbf{y}(A)$ into any presheaf $F$ are exactly the elements of $F(A)$.

> [!tip] Sheaves, Schemes, and Topos Theory *(from Algebraic Geometry and Logic)*
> A **sheaf** is a presheaf with a gluing condition; the category of sheaves on a site is a **topos**, a category that behaves like $\mathbf{Set}$ and serves as a universe for geometry and logic. A **scheme** is glued from affine pieces, each an [[Def - Hom-Functor and Representable Functor|affine scheme]] = representable functor; presheaves on $\mathbf{CRing}^{op}$ are the ambient world of the functor-of-points approach. The **subobject classifier** of a presheaf topos generalizes the two-element set of [[Def - Universal Element]].

> [!tip] Simplicial Sets and ∞-Categories *(from Higher Category Theory)*
> Presheaves on the simplex category $\Delta$ are **simplicial sets**, the carrier of homotopy-coherent structure. **Quasi-categories** (Joyal, Lurie) are simplicial sets with horn-filling conditions, the working model of $\infty$-categories. The presheaf-category formalism here is exactly what makes that theory possible.

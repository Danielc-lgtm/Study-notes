---
type: definition
subject: model-categories
prereqs:
  - "Def - Monoidal Category"
  - "Def - Cartesian Closed Category"
  - "Def - Adjunction"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $(\mathcal{C}, \otimes, I)$ is a [[Def - Monoidal Category|monoidal category]]: a category with a tensor functor $\otimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$, a unit object $I$, and coherent associator and unitor isomorphisms $\alpha, \lambda, \rho$. For objects $B, C$ we write $[B, C]$ (also $\underline{\mathrm{Hom}}(B, C)$ or $B \multimap C$) for the **internal hom**, and $\mathrm{ev} : [B, C] \otimes B \to C$ for the **evaluation** morphism. The hom-*set* of $\mathcal{C}$ is written $\mathcal{C}(A, B)$; the internal hom is an *object* of $\mathcal{C}$, distinct from the external hom-set. For $f : A \otimes B \to C$ its **transpose** (curried form) is $\widehat{f} : A \to [B, C]$. The full symbol registry is on [[Model Categories — Monoidal Model Categories]].

This is a compound page: it defines two interlocking notions — the **internal hom** $[B, C]$ and the **closed monoidal category** that has all of them — because the internal hom is the data and closedness is the property of possessing it for every $B$, with the evaluation/transpose machinery shared between them. A separate, brief notion of **biclosed** (closed on both the left and the right) is recorded for the non-symmetric case.

---

# Axiom Motivation

The motivation is to internalize the hom-set in the presence of a tensor product. In any [[Def - Monoidal Category|monoidal category]] the morphisms $B \to C$ form a *set* $\mathcal{C}(B, C)$, an external object living in $\mathbf{Set}$, not in $\mathcal{C}$. But in the richest examples there is an *object of $\mathcal{C}$* that deserves to be called "the object of maps from $B$ to $C$": for $R$-modules, the linear maps $M \to N$ form an $R$-module $\mathrm{Hom}_R(M, N)$; for vector spaces, $\mathrm{Hom}_k(V, W)$ is a vector space; for chain complexes, the maps form another chain complex. Closedness is the demand that this internal hom always exists and behaves correctly with respect to $\otimes$.

What should "behaves correctly" mean? The template is the **tensor-hom adjunction** you already know from module theory. A bilinear map $M \otimes_R N \to P$ — equivalently, an $R$-linear map out of the tensor product — is the same thing as an $R$-linear map $M \to \mathrm{Hom}_R(N, P)$, by fixing the first argument: this is the [[Thm - Universal Property of the Tensor Product of Modules|universal property of the tensor product]] read as an adjunction. The defining demand of closedness abstracts exactly this: a natural bijection
$$\mathcal{C}(A \otimes B, C) \;\cong\; \mathcal{C}(A, [B, C]) \qquad \text{natural in } A \text{ and } C.$$
But this is precisely the statement that the functor $- \otimes B$ has a **right adjoint** $[B, -]$. **Closedness is the demand that "tensor with $B$" be a left adjoint, for every $B$.** The internal hom is the right adjoint; currying is the adjunction transpose; evaluation $\mathrm{ev} : [B, C] \otimes B \to C$ is the counit.

Why phrase it as an adjunction rather than just "the object $[B, C]$ exists"? Because the adjunction is what makes $[B, C]$ an *object of $\mathcal{C}$* with the right universal property, not merely a set that happens to carry extra structure. The universal property is: there is $\mathrm{ev} : [B, C] \otimes B \to C$ such that every $f : A \otimes B \to C$ factors *uniquely* as $f = \mathrm{ev} \circ (\widehat{f} \otimes 1_B)$. Without uniqueness, $[B, C]$ would be merely *some* object admitting an evaluation, with no claim to represent the functor $\mathcal{C}(- \otimes B, C)$. Drop uniqueness and the bijection $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C])$ fails: you would have an evaluation map but multiple incompatible curryings.

Why require it for *every* $B$, not just some? Because closedness is a property of the *monoidal structure*, and a single internal hom is parochial. The strength of the notion is that it makes $[-,-]$ a functor of two variables, contravariant in the first and covariant in the second, with composition $[B, C] \otimes [A, B] \to [A, C]$ internalized — so $\mathcal{C}$ becomes **enriched over itself**. If you only had $[B_0, -]$ for one $B_0$ you could not compose internal homs, and the self-enrichment, which is the entire point, would collapse.

What breaks if the tensor is not symmetric? Then $- \otimes B$ and $B \otimes -$ are genuinely different functors, and each may have its own right adjoint. The right adjoint of $- \otimes B$ is the **right internal hom**; the right adjoint of $B \otimes -$ is the **left internal hom**. A category with both is **biclosed**; in the symmetric case they coincide and one speaks simply of *the* internal hom. The endofunctor category $([\mathcal{C}, \mathcal{C}], \circ)$ with composition as tensor is monoidal but *not* closed in general — there is no functor $[G, -]$ with $[\mathcal{C},\mathcal{C}](F \circ G, H) \cong [\mathcal{C},\mathcal{C}](F, [G, H])$ — which is exactly why "monoid in $[\mathcal{C},\mathcal{C}]$" (a monad) is a useful notion but "module over it via an internal hom" is not the right framing. Closedness is a real restriction, not a formality.

---

# The Definition

Let $(\mathcal{C}, \otimes, I)$ be a [[Def - Monoidal Category|monoidal category]].

An **internal hom** (right internal hom) of $C$ by $B$ is an object $[B, C]$ together with an **evaluation** morphism $\mathrm{ev} : [B, C] \otimes B \to C$ such that for every object $A$ and every morphism $f : A \otimes B \to C$ there is a *unique* morphism $\widehat{f} : A \to [B, C]$ (the **transpose** or **currying** of $f$) making the triangle commute:
$$\mathrm{ev} \circ (\widehat{f} \otimes 1_B) = f.$$

A monoidal category $\mathcal{C}$ is **(right) closed** if an internal hom $[B, C]$ exists for every pair of objects $B, C$. Equivalently: for every object $B$ the functor $- \otimes B : \mathcal{C} \to \mathcal{C}$ has a right adjoint $[B, -]$, exhibited by a natural isomorphism
$$\mathcal{C}(A \otimes B, C) \;\cong\; \mathcal{C}(A, [B, C]) \qquad \text{natural in } A \text{ and } C.$$
The counit of this adjunction is evaluation $\mathrm{ev} : [B, C] \otimes B \to C$; the transpose $\widehat{f}$ is the adjunction's transpose.

$\mathcal{C}$ is **left closed** if instead each $B \otimes -$ has a right adjoint, and **biclosed** if it is both left and right closed. A **closed symmetric monoidal category** is a symmetric monoidal category that is closed; symmetry makes the left and right internal homs coincide, so there is a single $[-, -]$, and this is the default meaning of "closed monoidal" in homotopy theory (and in this chapter).

---

# Categorical / Structural Definition

The cleanest structural reading is **self-enrichment**. A closed monoidal category $\mathcal{C}$ is canonically enriched over itself: the hom-*object* $[B, C]$ replaces the hom-set, composition is the internal morphism
$$[B, C] \otimes [A, B] \xrightarrow{\ \circ\ } [A, C]$$
(obtained by transposing $\mathrm{ev} \circ (1 \otimes \mathrm{ev}) : [B,C] \otimes [A,B] \otimes A \to C$), and the identity of $A$ is the transpose $I \to [A, A]$ of the unitor $\lambda_A : I \otimes A \to A$. So a closed monoidal category is precisely a monoidal category that is a [[Def - Enriched Category|category enriched over itself]] in a way compatible with $\otimes$. The external hom-set is recovered as $\mathcal{C}(B, C) \cong \mathcal{C}(I, [B, C])$ — "global elements of the internal hom" — which is the categorical content of "a morphism $B \to C$ is a point of the object of maps $B \to C$".

A second structural fact, by [[Thm - Right Adjoints Preserve Limits|RAPL]] and its dual: since $[B, -]$ is a right adjoint it **preserves limits**, giving $[B, \textstyle\prod_i C_i] \cong \prod_i [B, C_i]$; and since $- \otimes B$ is a left adjoint it **preserves colimits**, giving $(\coprod_i A_i) \otimes B \cong \coprod_i (A_i \otimes B)$. The latter is the abstract "tensor distributes over direct sums" you know from module theory, and it is automatic from closedness alone — you never have to check it by hand.

The relation to the cartesian case is exact: a [[Def - Cartesian Closed Category|cartesian closed category]] is a closed monoidal category whose tensor is the categorical product $\times$ (so $I$ is the terminal object $1$ and $[B, C] = C^B$ is the exponential). "Cartesian closed" is "closed with respect to the product"; closed monoidal is the same demand for a general $\otimes$.

---

# Relate to Other Fields / Compression

A closed monoidal category is the abstraction that unifies three "function-object" constructions you already know. In $\mathbf{Set}$ (cartesian, $\otimes = \times$) the internal hom is the function set $C^B$ — this is a [[Def - Cartesian Closed Category|CCC]]. In $\mathbf{Mod}_R$ (non-cartesian, $\otimes = \otimes_R$) the internal hom is $\mathrm{Hom}_R(B, C)$ with its $R$-module structure, and the adjunction is the [[Def - Tensor Product of Modules|tensor-hom adjunction]] — closed but *not* cartesian closed, since the monoidal product is $\otimes_R$, not the categorical product $\oplus$. In $\mathbf{Cat}$ (cartesian) the internal hom is the functor category $[\mathcal{B}, \mathcal{C}]$. The single statement $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C])$ specializes to "currying", "the tensor-hom adjunction", and "the exponential law for functor categories" in turn.

**True name:** *closed monoidal means "tensor with $B$ has a right adjoint, for every $B$", i.e. you can curry along $\otimes$.* The operational content is the bijection $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C])$ — a map *out of a tensor* is a map *into an internal hom*. When you ask "is this monoidal category closed?", you are asking "can I always internalize the hom-set as an object, with evaluation and currying compatible with $\otimes$?". And the reflex it should trigger: *whenever a condition involves $\otimes$ on the source, transpose it to a condition involving $[-,-]$ on the target* — this is exactly the move that, in the homotopical setting, turns the pushout-product axiom into the pullback-hom condition.

---

# Examples / Corollaries

**Is an instance — $\mathbf{Set}$ with $\times$.** The internal hom is the function set $C^B$; evaluation is $(\phi, b) \mapsto \phi(b)$; currying is ordinary currying. This is the cartesian closed prototype, $|C^B| = |C|^{|B|}$.

**Is an instance — $\mathbf{Mod}_R$ with $\otimes_R$.** For a commutative ring $R$, the internal hom is $\mathrm{Hom}_R(M, N)$, the $R$-module of $R$-linear maps, and the adjunction $\mathcal{C}(L \otimes_R M, N) \cong \mathcal{C}(L, \mathrm{Hom}_R(M, N))$ is the [[Def - Tensor Product of Modules|tensor-hom adjunction]]. This is the canonical *non-cartesian* example and the one to keep in mind throughout this chapter: it is closed monoidal but its monoidal product $\otimes_R$ is not the categorical product (which is $\oplus$ for finitely many factors). The categorical content of "the internal hom is a module too" is exactly self-enrichment.

**Is an instance — $\mathbf{Ch}(R)$ with $\otimes_R$.** Chain complexes form a closed symmetric monoidal category: $(M \otimes_R N)_n = \bigoplus_{p+q=n} M_p \otimes_R N_q$ with the Koszul-sign differential, and the internal hom $[M, N]$ is the complex with $[M, N]_n = \prod_p \mathrm{Hom}_R(M_p, N_{p+n})$. The unit is $R$ concentrated in degree zero. This is the example whose *homotopical* refinement — derived tensor and Tor — drives the rest of the chapter.

**Is an instance — $\mathbf{sSet}$ with $\times$.** Simplicial sets are cartesian closed: the internal hom $[X, Y]$ (the "function complex") has $n$-simplices $[X, Y]_n = \mathbf{sSet}(X \times \Delta^n, Y)$. The unit is $\Delta^0$, the terminal object. Cartesian closure of $\mathbf{sSet}$ is what makes mapping spaces available and underlies the simplicial enrichment of homotopy theory.

**Is NOT an instance — $\mathbf{Top}$ with $\times$.** The category of all topological spaces with the product topology is monoidal but **not** cartesian closed: there is in general no topology on the set $C(B, C)$ of continuous maps making evaluation continuous *and* currying a bijection for every space $A$. The failure is the classical reason one passes to **compactly generated weak Hausdorff** spaces, where the $k$-ification of the compact-open topology repairs closedness. So "has products" does not imply "closed".

**Is NOT an instance — the endofunctor category $([\mathcal{C}, \mathcal{C}], \circ)$.** Composition of endofunctors is a monoidal product (this is where monads live, as [[Def - Monoid in a Monoidal Category|monoids]]), but it is *not* closed: $- \circ G$ has no right adjoint in general, because composition does not preserve colimits in the left variable. This is why one does not speak of an "internal hom of functors with respect to composition", and a structural reason monads are studied through their algebras rather than through an internal-hom calculus.

**Calibration check.** Verify that in any closed monoidal category $\mathcal{C}(B, C) \cong \mathcal{C}(I, [B, C])$ (apply the defining adjunction with $A = I$ and use the unitor $I \otimes B \cong B$). Verify that $[I, C] \cong C$ (the internal hom out of the unit is the object itself) and that $- \otimes B$ preserves all coproducts (it is a left adjoint). If you can explain *why* $\mathbf{Mod}_R$ is closed monoidal but not cartesian closed — its monoidal product $\otimes_R$ is not the categorical product $\oplus$ — you have understood the distinction at the heart of this chapter.

---

# Unlocked by This

> [!tip] Monoidal Model Category *(from this chapter)*
> Closedness is the precondition for the whole chapter: only a [[Def - Closed Monoidal Category|closed monoidal category]] has the internal hom $[-,-]$ whose **pullback-hom** (Leibniz cotensor) is the adjoint of the **pushout-product**. A [[Def - Monoidal Model Category|monoidal model category]] is a closed (symmetric) monoidal category equipped with a compatible model structure, and the pushout-product axiom is statable in this generality precisely because the internal hom is available to transpose against.

> [!tip] Models of Linear Logic *(from Logic and Type Theory)*
> A closed symmetric monoidal category is the categorical semantics of **multiplicative intuitionistic linear logic**: $\otimes$ is the multiplicative conjunction, $[B, C]$ is linear implication $B \multimap C$, and the lack of a diagonal $A \to A \otimes A$ models the prohibition on duplicating resources. This is the Curry-Howard-Lambek correspondence one step beyond the cartesian closed (intuitionistic) case.

> [!tip] Enrichment and the Internal Language *(from Higher Category Theory)*
> A closed monoidal category is **enriched over itself**, and choosing a closed monoidal base $\mathcal{V}$ is exactly choosing the values in which a [[Def - Enriched Category|$\mathcal{V}$-enriched category]] takes its hom-objects. Taking $\mathcal{V} = \mathbf{sSet}$ gives simplicially enriched categories, a model for **∞-categories**; the closed monoidal structure on $\mathcal{V}$ is what makes the enriched composition and the homotopy theory of enriched categories possible.

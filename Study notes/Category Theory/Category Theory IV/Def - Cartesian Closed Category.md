---
type: definition
subject: category-theory
prereqs:
  - "Def - Adjunction"
  - "Def - Product and Coproduct"
  - "Def - Initial and Terminal Object"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a category with finite [[Def - Product and Coproduct|products]]: a [[Def - Initial and Terminal Object|terminal object]] $1$ (the empty product) and binary products $A \times B$. For objects $B, C$ we write $C^B$ (also $[B, C]$ or $B \Rightarrow C$) for the **exponential** of $C$ by $B$, and $\mathrm{ev} : C^B \times B \to C$ for the **evaluation** morphism. For $f : A \times B \to C$, its **transpose** (curried form) is written $\widehat{f} : A \to C^B$ (also $\lambda f$); for $g : A \to C^B$ the transpose is $\widetilde{g} : A \times B \to C$. The full symbol registry is on [[Category Theory IV — Adjunctions]].

This page defines two interlocking notions — the **exponential object** $C^B$ and the **cartesian closed category** that has all of them — because the exponential is the data and cartesian closure is the property of having it for every pair, with the evaluation/transpose machinery shared between them.

---

# Axiom Motivation

The motivation is to internalise the hom-set. In any category, the morphisms $B \to C$ form a *set* $\mathcal{C}(B, C)$ — an external object, living in $\mathbf{Set}$, not in $\mathcal{C}$. But often there is an *object of $\mathcal{C}$* that deserves to be called "the object of maps from $B$ to $C$": in $\mathbf{Set}$ the set $C^B$ of functions is again a set; in $\mathbf{Vect}_k$ the linear maps $V \to W$ form a vector space; in $\mathbf{Cat}$ the functors $\mathcal{B} \to \mathcal{C}$ form a category (the functor category). Cartesian closure is the property that this **internal hom** always exists and behaves correctly.

What should "behaves correctly" mean? Look at $\mathbf{Set}$ for the template. A function of two arguments $f : A \times B \to C$ can be **curried**: fix the first argument $a$ and you get a function $b \mapsto f(a, b)$ in $C^B$; letting $a$ vary gives $\widehat{f} : A \to C^B$. This is a bijection — every $g : A \to C^B$ uncurries to $\widetilde{g}(a, b) = g(a)(b)$, and currying then uncurrying is the identity. So the defining demand is the natural bijection
$$\mathcal{C}(A \times B, C) \;\cong\; \mathcal{C}(A, C^B) \qquad \text{natural in } A.$$
But this is exactly the statement that the functor $(-) \times B$ has a **right adjoint** $(-)^B$. **Cartesian closure is the demand that "product with $B$" be a left adjoint, for every $B$.** The exponential is the right adjoint; currying is the adjunction transpose; evaluation $\mathrm{ev} : C^B \times B \to C$ is the counit.

Why phrase it as an adjunction rather than just "the set $C^B$ exists"? Because the adjunction is what makes $C^B$ an *object of $\mathcal{C}$* with the right universal property, not merely a set. The universal property of $C^B$ is: there is $\mathrm{ev} : C^B \times B \to C$ such that every $f : A \times B \to C$ factors *uniquely* as $f = \mathrm{ev}\circ(\widehat{f}\times 1_B)$. Without uniqueness, $C^B$ would just be *some* object admitting an evaluation, with no claim to be *the* object of maps; uniqueness (the adjunction's bijectivity) is what pins it down. Drop uniqueness and you lose the bijection $\mathcal{C}(A\times B, C) \cong \mathcal{C}(A, C^B)$ — you would have an evaluation map but multiple incompatible "curryings", so $C^B$ would not represent the functor $\mathcal{C}(- \times B, C)$.

Why insist on finite *products* first? Because the exponential's universal property is stated using $A \times B$ on the left. The product is the *context* in which a "function of an extra argument $B$" lives; you cannot say "a map of two arguments" without a product to package the two arguments. The terminal object $1$ is needed too, as the empty product, and it forces $C^1 \cong C$ (a function from a one-point object is just a point of $C$) and $1^B \cong 1$ (there is exactly one function to a point). What breaks if products are missing? You cannot even form $C^B \times B$ to write down evaluation, so the definition does not get off the ground. What breaks if you have products but *not* exponentials? You have a cartesian category but cannot internalise hom — $\mathbf{Top}$ is the standard cautionary tale: it has products but is **not** cartesian closed (there is no topology on the set of continuous maps making evaluation continuous and currying a bijection for all spaces; one must pass to compactly generated spaces to repair it).

A last design point: why is the exponential a *right* adjoint and not a left one? Because "maps *into* $C^B$" is the easy side (they are maps $A \times B \to C$), so $C^B$ sits on the right of the hom-set and $(-)\times B$ on the left. The handedness has teeth: by [[Thm - Right Adjoints Preserve Limits|RAPL]], $(-)^B$ preserves limits, giving $\left(\prod_i C_i\right)^B \cong \prod_i C_i^B$ and $(C \times D)^B \cong C^B \times D^B$; and by LAPC, $(-)\times B$ preserves colimits, giving the distributive law $A \times (X \sqcup Y) \cong (A\times X) \sqcup (A \times Y)$ in any cartesian closed category with coproducts.

---

# The Definition

Let $\mathcal{C}$ be a category with finite [[Def - Product and Coproduct|products]]. For objects $B, C$, an **exponential** of $C$ by $B$ is an object $C^B$ together with an **evaluation** morphism $\mathrm{ev} : C^B \times B \to C$ such that for every object $A$ and every morphism $f : A \times B \to C$ there is a *unique* morphism $\widehat{f} : A \to C^B$ (the **transpose** or **currying** of $f$) making the triangle commute:
$$\mathrm{ev} \circ (\widehat{f} \times 1_B) = f.$$

A category $\mathcal{C}$ is **cartesian closed** (a **CCC**) if it has a terminal object, all binary products, and an exponential $C^B$ for every pair of objects $B, C$. Equivalently: $\mathcal{C}$ has finite products, and for every object $B$ the functor $(-)\times B : \mathcal{C} \to \mathcal{C}$ has a right adjoint $(-)^B$:
$$\mathcal{C}(A \times B, C) \;\cong\; \mathcal{C}(A, C^B) \qquad \text{natural in } A \text{ and } C.$$
The counit of this adjunction is evaluation $\mathrm{ev} : C^B \times B \to C$; the transpose $\widehat{f}$ is the adjunction's transpose of $f$.

---

# Categorical / Structural Definition

A CCC is a model of the simply typed **lambda calculus** and of intuitionistic propositional logic; this is the **Curry-Howard-Lambek correspondence**, and it is best regarded as the *structural* definition. Read the data as follows:

- **Objects $=$ types $=$ propositions.** Each object is a type (in the calculus) or a proposition (in logic).
- **Morphisms $A \to B$ $=$ terms/programs of type $A \to B$ $=$ proofs of $A \vdash B$.** Composition is substitution/cut.
- **The terminal object $1$ $=$ the unit type $=$ the proposition "true"** ($\top$).
- **Products $A \times B$ $=$ pair types $=$ conjunction $A \wedge B$.** Projections are the two eliminations of a conjunction.
- **Exponentials $C^B$ $=$ function types $B \to C$ $=$ implication $B \Rightarrow C$.** Evaluation is *modus ponens* / function application; currying is the **deduction theorem** ($A \wedge B \vdash C$ iff $A \vdash B \Rightarrow C$) and $\lambda$-abstraction.

The bijection $\mathcal{C}(A \times B, C) \cong \mathcal{C}(A, C^B)$ is simultaneously the deduction theorem and the typing rule for $\lambda$-abstraction. The free CCC on a set of base types *is* the simply typed lambda calculus; this is the sense in which "the lambda calculus is the internal language of cartesian closed categories". When $\mathcal{C}$ is a poset, a CCC is exactly a [[Def - Initial and Terminal Object|Heyting algebra]]: finite meets ($\wedge$), the exponential being the **Heyting implication** $a \Rightarrow b = \bigvee\{c : c \wedge a \leq b\}$, with $a \wedge (a \Rightarrow b) \leq b$ the evaluation. Boolean algebras are the special Heyting algebras where $\neg\neg a = a$; the failure of that law in a general Heyting algebra is the failure of the law of excluded middle in intuitionistic logic.

---

# Relate to Other Fields / Compression

A CCC is the cartesian (product-based) special case of a **closed monoidal category**: replace the cartesian product $\times$ by a general monoidal product $\otimes$ and the exponential $C^B$ by an internal hom $[B, C]$ with $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B,C])$, and you have a closed monoidal category. The [[Def - Tensor Product of Modules|tensor-hom adjunction]] $- \otimes_R M \dashv \mathrm{Hom}_R(M, -)$ exhibits $\mathbf{Mod}_R$ as closed monoidal (but *not* cartesian closed — its monoidal product is $\otimes$, not the categorical product $\oplus$). So "cartesian closed" is "closed with respect to the product"; many categories are closed for $\otimes$ without being closed for $\times$.

**True name:** *cartesian closed means "product with $B$ has a right adjoint, for every $B$", i.e. you can curry.* The operational content is the bijection $\mathcal{C}(A \times B, C) \cong \mathcal{C}(A, C^B)$ — a map of two arguments is a map of one argument valued in maps of the other. When you ask "is this category cartesian closed?", you are asking "can I always internalise the hom-set as an object, with evaluation and currying?".

---

# Examples / Corollaries

**Is an instance — $\mathbf{Set}$.** $C^B$ is the set of all functions $B \to C$; evaluation is $(\phi, b) \mapsto \phi(b)$; currying is the usual currying of a two-variable function. The cardinality $|C^B| = |C|^{|B|}$ is the reason for the exponential notation. This is the template every other example imitates.

**Is an instance — $\mathbf{Cat}$.** For small categories, $\mathcal{C}^{\mathcal{B}}$ is the [[Def - Functor Category|functor category]] $[\mathcal{B}, \mathcal{C}]$ — functors $\mathcal{B} \to \mathcal{C}$ as objects, [[Def - Natural Transformation|natural transformations]] as morphisms. Evaluation $[\mathcal{B},\mathcal{C}] \times \mathcal{B} \to \mathcal{C}$ sends a functor and an object to the functor's value. So "the category of functors is an exponential" is the precise statement that $\mathbf{Cat}$ is cartesian closed.

**Is an instance — every presheaf category.** $[\mathcal{C}^{op}, \mathbf{Set}]$ is cartesian closed for any small $\mathcal{C}$; the exponential is computed pointwise-with-a-twist via the Yoneda lemma, $(Q^P)(c) \cong [\mathcal{C}^{op}, \mathbf{Set}](\mathbf{y}c \times P, Q)$. This is why **topoi** (which are particular presheaf-like categories) are cartesian closed — a defining feature of a topos.

**Is an instance — a Heyting algebra.** A poset with finite meets and joins and a Heyting implication $a \Rightarrow b$ satisfying $c \leq (a \Rightarrow b) \iff c \wedge a \leq b$ is exactly a cartesian closed poset. The opens of a topological space form a Heyting algebra: $U \Rightarrow V = \mathrm{int}((X\setminus U)\cup V)$. This is the order-theoretic shadow of the lambda calculus.

**Is NOT an instance — $\mathbf{Top}$.** The category of all topological spaces has finite products but is **not** cartesian closed: there is in general no topology on the set of continuous maps $C(B, C)$ making evaluation continuous and currying a bijection for *all* spaces $A$. (The compact-open topology works only when $B$ is locally compact Hausdorff.) The fix is to restrict to **compactly generated** spaces, which form a cartesian closed category — this is exactly why algebraic topologists work there.

**Is NOT an instance — $\mathbf{Grp}$ or $\mathbf{Vect}_k$ (as cartesian closed).** $\mathbf{Vect}_k$ has products (which coincide with coproducts, the direct sum, in the finite case) but is not cartesian closed: there is no vector space $W^V$ with $\mathbf{Vect}(U \times V, W) \cong \mathbf{Vect}(U, W^V)$, because a linear map out of a product $U \oplus V$ is a *pair* of linear maps, not a map of two arguments — the right notion of "two-argument map" is *bilinear*, which lives over $U \otimes V$, not $U \oplus V$. So $\mathbf{Vect}_k$ is closed *monoidal* for $\otimes$ but not cartesian closed for $\times$. This is the sharpest illustration that cartesian closure is about the *product*, not just about having an internal hom.

**Corollary — exponential laws.** In any CCC: $C^1 \cong C$, $1^B \cong 1$, $(C \times D)^B \cong C^B \times D^B$ (right adjoint preserves products), $C^{B \times B'} \cong (C^B)^{B'}$ (iterated currying), and $A \times(X \sqcup Y) \cong (A\times X)\sqcup(A\times Y)$ when coproducts exist ($(-)\times B$ preserves colimits). These are the categorical versions of the arithmetic of exponents.

**Calibration check.** Verify that currying then uncurrying is the identity in $\mathbf{Set}$, i.e. $\widetilde{(\widehat{f})} = f$. Confirm the exponential law $C^{B\times B'} \cong (C^B)^{B'}$ from iterating the adjunction. Explain in one sentence why $\mathbf{Vect}_k$ fails to be cartesian closed even though it has an internal hom.

---

# Unlocked by This

> [!tip] Curry-Howard-Lambek and the Internal Language *(from Logic / Type Theory — Cluster 10)*
> A CCC is a model of the simply typed lambda calculus: **objects = types = propositions**, **morphisms = programs = proofs**, **products = conjunction = pair types**, **exponentials = implication = function types**. The free CCC on a set of base types is the calculus itself. This **Curry-Howard-Lambek** correspondence is the foundation of categorical logic and the launching point for dependent type theory and proof assistants. See [[Ex - Curry-Howard-Lambek correspondence]].

> [!tip] Locally Cartesian Closed Categories and Dependent Types *(from Type Theory / Topos Theory)*
> When *every slice category* $\mathcal{C}/A$ is cartesian closed, $\mathcal{C}$ is **locally cartesian closed** (LCCC); the slice exponentials model **dependent product types** ($\Pi$) and pullback models substitution. Every **topos** is LCCC. Pushing this to the homotopical setting gives the categorical semantics of **homotopy type theory**, where identity types add a notion of path.

> [!tip] Closed Monoidal Categories, Enrichment, and TQFT *(from Monoidal / Enriched Category Theory)*
> Replacing $\times$ by a monoidal $\otimes$ gives a **closed monoidal category** with internal hom $[B,C]$; this is the setting for **enriched category theory** (hom-objects live in $\mathcal{C}$), for the **symmetric monoidal categories** of **categorical probability** and **TQFT**, and for the string-diagram calculus the user's research uses.

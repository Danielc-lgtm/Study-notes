---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Enriched Category"
  - "Def - Monoidal Category"
  - "Def - Vector Space"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that a category enriched in $(\mathbf{Vect}_k, \otimes_k, k)$ — the [[Def - Monoidal Category|monoidal category]] of [[Def - Vector Space|$k$-vector spaces]] under tensor product — is exactly a **$k$-linear category**: an ordinary category in which each hom-set is a $k$-vector space and composition is $k$-bilinear. Then prove the **one-object** case is a $k$-algebra, with the single hom-space as the underlying vector space, composition as multiplication, and the enriched identity as the algebra unit.

**Recall:**

![[Def - Enriched Category#The Definition]]

The monoidal category $(\mathbf{Vect}_k,\otimes_k,k)$ has [[Def - Vector Space|$k$-vector spaces]] as objects, $k$-linear maps as morphisms, tensor product $\otimes_k$ as monoidal product, and the ground field $k$ (as a one-dimensional space) as unit. A linear map out of a tensor product $V\otimes_k W$ is the same as a $k$-bilinear map out of $V\times W$ (universal property, [[Thm - Universal Property of the Tensor Product]]). A $k$-algebra is a vector space $R$ with an associative bilinear multiplication and a unit $1\in R$.

---

# Convergent Strategy

**Problem class:** This is an "identification by unwinding" problem, the first source pattern of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]], and the linear twin of [[Ex - An Ab-enriched category is a preadditive category|the $\mathbf{Ab}$-enriched exercise]]. Substitute $\mathcal{V}=\mathbf{Vect}_k$ into [[Def - Enriched Category|the enriched definition]] and read off the result.

**Assumption pattern:** The recognisable feature is "hom-objects in $\mathbf{Vect}_k$" with monoidal product $\otimes_k$. The two structural facts that carry content are: a morphism out of $\otimes_k$ is a bilinear map (forcing bilinear composition), and the unit object is the *ground field* $k$ (so the enriched identity is a linear map $k\to\mathcal{C}(A,A)$, i.e. a scalar multiple, picking out $1_A$).

**Theorem routing:** The route is the universal property of the tensor product ([[Thm - Universal Property of the Tensor Product]]): linear maps $V\otimes_k W\to U$ correspond to bilinear maps $V\times W\to U$. Applied to enriched composition this gives $k$-bilinearity; the one-object case then matches the $k$-algebra axioms directly.

**Key decision point:** The non-obvious choice is recognising that the enriched identity, a map $k\to\mathcal{C}(A,A)$, is *more* than picking an element — it is a whole one-dimensional subspace of scalar multiples of $1_A$, which is exactly the image of the field $k$ inside the algebra under "$\lambda\mapsto\lambda\cdot 1$". This is what makes the one-object case a *unital* algebra over $k$, not merely a ring.

---

# Legal Operations Used

1. **Operation 1 (unwind an enriched definition in the base).** Substitute $\mathcal{V}=\mathbf{Vect}_k$ and translate the data and axioms into linear-algebra language.

2. **Operation 6 (recognise a one-object case as a monoid-like structure).** The single hom-space with bilinear composition and unit is a $k$-algebra.

---

# Hints

> [!note]- Hint 1
> Each hom-object $\mathcal{C}(A,B)$ is a $k$-vector space. The composition morphism is a *linear map* — out of what space, and to where?

> [!note]- Hint 2
> Composition is linear out of $\mathcal{C}(B,C)\otimes_k\mathcal{C}(A,B)$. By the universal property of $\otimes_k$, that is the same as a bilinear map out of $\mathcal{C}(B,C)\times\mathcal{C}(A,B)$: composition is $k$-bilinear, $\lambda(g\circ f)=(\lambda g)\circ f=g\circ(\lambda f)$ and additive in each slot.

> [!note]- Hint 3
> The enriched identity is a linear map $k\to\mathcal{C}(A,A)$, determined by the image of $1\in k$, namely $1_A$; linearity means $\lambda\mapsto\lambda\cdot 1_A$. With one object, the hom-space is the algebra, composition is multiplication, and $1_\star$ is the unit.

---

# Solution

The plan: Step 1 reads off the linear structure on hom-sets. Step 2 derives bilinear composition from the tensor's universal property. Step 3 reads off the identity. Step 4 specialises to one object and matches the $k$-algebra axioms.

**Step 1: Hom-spaces and the underlying category.** Each $\mathcal{C}(A,B)$ is a $k$-vector space; forgetting the vector-space structure gives an ordinary category, and remembering it equips hom-sets with addition and scalar multiplication.

> [!note]- Derivation
> The enriched data gives, for each pair, a hom-object $\mathcal{C}(A,B)\in\mathbf{Vect}_k$ — a $k$-vector space. Forgetting to the underlying set (apply $\mathbf{Vect}_k(k,-)$, which returns the underlying set of vectors) gives an ordinary category. The retained structure is that each hom-set carries vector addition, a zero morphism, and scalar multiplication by $k$.

**Step 2: Composition is $k$-bilinear.** Composition is a linear map $\mathcal{C}(B,C)\otimes_k\mathcal{C}(A,B)\to\mathcal{C}(A,C)$; by the universal property of $\otimes_k$ this is a $k$-bilinear map, so composition distributes over addition and commutes with scalars in each variable.

> [!note]- Derivation
> By [[Def - Enriched Category|definition]] composition is a morphism of $\mathcal{V}=\mathbf{Vect}_k$, hence a *linear map* $c:\mathcal{C}(B,C)\otimes_k\mathcal{C}(A,B)\to\mathcal{C}(A,C)$. The universal property of the tensor product ([[Thm - Universal Property of the Tensor Product]]) identifies linear maps out of $V\otimes_k W$ with $k$-bilinear maps out of $V\times W$. Writing $g\circ f$ for the image of $g\otimes f$, bilinearity reads
> $$(g_1+g_2)\circ f = g_1\circ f+g_2\circ f,\quad g\circ(f_1+f_2)=g\circ f_1+g\circ f_2,\quad \lambda(g\circ f)=(\lambda g)\circ f=g\circ(\lambda f),$$
> for $\lambda\in k$. This is exactly the definition of a $k$-linear category. Associativity and unit axioms unwind to the ordinary ones (compatible with the linear structure).

**Step 3: The identity.** The enriched identity is a linear map $j_A:k\to\mathcal{C}(A,A)$, $\lambda\mapsto\lambda\cdot 1_A$ where $1_A:=j_A(1)$.

> [!note]- Derivation
> A linear map $k\to\mathcal{C}(A,A)$ is determined by the image of $1\in k$ (since $k$ is one-dimensional, spanned by $1$); set $1_A:=j_A(1)$, so $j_A(\lambda)=\lambda\cdot 1_A$. The enriched unit axiom unwinds (via the unitor $k\otimes V\cong V$) to $1_A\circ f=f=f\circ 1_B$, the ordinary identity laws. So the structure is a $k$-linear category.

**Step 4: One-object case is a $k$-algebra.** With a single object $\star$, the hom-space $R:=\mathcal{C}(\star,\star)$ is a $k$-vector space with bilinear, associative multiplication (composition) and unit $1_\star$ — a $k$-algebra.

> [!note]- Derivation
> One object leaves a single hom-object $R=\mathcal{C}(\star,\star)\in\mathbf{Vect}_k$. Composition is a bilinear map $R\times R\to R$ (Step 2) — an associative multiplication; the identity $j_\star:k\to R$, $\lambda\mapsto\lambda\cdot 1_\star$, is the unit map of the algebra, so $1_\star$ is a two-sided multiplicative unit and scalars act as $\lambda\cdot r=(\lambda 1_\star)r$. These are exactly the axioms of a unital associative $k$-algebra. Hence "$k$-algebra = one-object $k$-linear category", the linear analogue of "monoid = one-object category" and of "ring = one-object preadditive category".

> [!note]- Complete formal solution
> Let $\mathcal{C}$ be enriched in $(\mathbf{Vect}_k,\otimes_k,k)$.
>
> - *Hom-spaces:* each $\mathcal{C}(A,B)$ is a $k$-vector space; forgetting gives an ordinary category with vector-space hom-sets.
> - *Bilinear composition:* composition is linear out of $\mathcal{C}(B,C)\otimes_k\mathcal{C}(A,B)$, hence (universal property of $\otimes_k$) $k$-bilinear.
> - *Identities:* $j_A:k\to\mathcal{C}(A,A)$, $\lambda\mapsto\lambda 1_A$; unit and associativity axioms are the ordinary ones.
>
> This is precisely a $k$-linear category. With one object, the single hom-space is a $k$-algebra (composition = multiplication, $1_\star$ = unit, scalars from $j_\star$). $\quad\blacksquare$

---

# Key Takeaways

**The "monoid in $\mathcal{V}$" pattern is uniform: one-object $\mathcal{V}$-category = monoid object in $\mathcal{V}$.** Over $\mathbf{Set}$ it is a monoid; over $\mathbf{Ab}$ a ring; over $\mathbf{Vect}_k$ a $k$-algebra; over $\mathbf{Cat}$ a [[Def - Monoidal Category|monoidal category]]. In each case the single hom-object is the monoid object and composition is its multiplication. This is one of the most reusable recognitions in the chapter: whenever a structure is "one object's worth of data with an associative unital binary operation", it is a monoid in some monoidal category, and identifying that $\mathcal{V}$ tells you what kind of structure you have and what general theory applies.

**Tensor products convert "linear" into "bilinear automatically" — and that is the entire point of enriching over $\mathbf{Vect}_k$.** Just as for $\mathbf{Ab}$, the content lives in $\otimes_k$: composition is required to be linear *out of the tensor*, and the universal property makes that exactly bilinearity, with no separate check. The trigger-reaction to keep: "linear map out of $V\otimes_k W$" reads as "bilinear map on $V\times W$". This single fact powers the theory of algebras, bimodules, the [[Thm - Universal Property of the Tensor Product|tensor product]], and $k$-linear / dg-categories.

**$k$-linear categories are the substrate of representation theory and (one rung up) of dg- and stable categories.** A $k$-linear category is where you do representation theory "with several objects at once": the category of representations of a quiver, the category of modules over a $k$-algebra, the category of coherent sheaves on a variety. Enriching the *homs* in chain complexes rather than plain vector spaces gives a **dg-category**, and passing to its homotopy theory gives the **stable ∞-categories** and **derived categories** of §H.2 and §H.5. Recognising "$k$-linear category" as $\mathbf{Vect}_k$-enrichment places it at the base of that tower and lets the general enriched machinery be brought to bear immediately.

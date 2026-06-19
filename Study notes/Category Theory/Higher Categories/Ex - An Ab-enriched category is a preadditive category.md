---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Enriched Category"
  - "Def - Monoidal Category"
  - "Def - Abelian Group"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that a category enriched in $(\mathbf{Ab}, \otimes_{\mathbb{Z}}, \mathbb{Z})$ — the [[Def - Monoidal Category|monoidal category]] of [[Def - Abelian Group|abelian groups]] under tensor product — is exactly a **preadditive category**: an ordinary category in which each hom-set is an abelian group and composition is **bilinear** (biadditive),
$$(g_1 + g_2)\circ f = g_1\circ f + g_2\circ f, \qquad g\circ(f_1 + f_2) = g\circ f_1 + g\circ f_2.$$
Identify what the enriched composition morphism and the enriched identity morphism become, and explain why bilinearity (rather than mere additivity in one variable) is forced.

**Recall:**

![[Def - Enriched Category#The Definition]]

The monoidal category $(\mathbf{Ab},\otimes_{\mathbb{Z}},\mathbb{Z})$ has [[Def - Abelian Group|abelian groups]] as objects, group homomorphisms as morphisms, tensor product $\otimes_{\mathbb{Z}}$ as monoidal product, and the integers $\mathbb{Z}$ as unit. A homomorphism out of a tensor product $M\otimes_{\mathbb{Z}} N$ is the same as a $\mathbb{Z}$-**bilinear** map out of $M\times N$ (the universal property of $\otimes$).

---

# Convergent Strategy

**Problem class:** This is an "identification by unwinding" problem, the first source pattern in the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]]. The routine is mechanical: substitute $\mathcal{V} = \mathbf{Ab}$ into [[Def - Enriched Category|the enriched-category definition]] and read off what each piece of data and each axiom becomes in the concrete language of abelian groups.

**Assumption pattern:** The recognisable feature is "hom-objects in $\mathbf{Ab}$" — each $\mathcal{C}(A,B)$ is an abelian group. The decisive structural fact about $\mathbf{Ab}$ is that its monoidal product is $\otimes_{\mathbb{Z}}$, *not* the cartesian product; this is what turns "composition is a morphism of $\mathcal{V}$" into "composition is bilinear".

**Theorem routing:** The route is the universal property of the tensor product (see [[Thm - Universal Property of the Tensor Product]] for the vector-space version, [[Thm - Universal Property of the Tensor Product of Modules]] for modules): a group homomorphism $M\otimes_{\mathbb{Z}} N \to P$ corresponds to a bilinear map $M\times N\to P$. Applying this to the enriched composition $\mathcal{C}(B,C)\otimes\mathcal{C}(A,B)\to\mathcal{C}(A,C)$ gives bilinearity.

**Key decision point:** The non-obvious choice is recognising that the *tensor* — not the cartesian product — is what carries the content. If one mistakenly enriched over $(\mathbf{Ab},\times)$ (the cartesian monoidal structure), composition would be merely a function $\mathcal{C}(B,C)\times\mathcal{C}(A,B)\to\mathcal{C}(A,C)$ with no linearity constraint. It is the choice $\otimes_{\mathbb{Z}}$ that forces bilinearity, and seeing this is the heart of the exercise.

---

# Legal Operations Used

1. **Operation 1 (unwind an enriched definition in the base).** We substitute $\mathcal{V}=\mathbf{Ab}$ and translate the composition morphism, identity morphism, and axioms into abelian-group language.

2. **Operation 6 (recognise a one-object case).** As a corollary we note a one-object $\mathbf{Ab}$-category is a *ring*: one abelian group with bilinear multiplication and a unit — exactly the ring axioms.

---

# Hints

> [!note]- Hint 1
> Each hom-object $\mathcal{C}(A,B)$ is an abelian group, so a hom-set with an addition. What is the *type* of the composition morphism in $\mathbf{Ab}$, and what is its domain?

> [!note]- Hint 2
> The composition morphism is a *homomorphism* $\mathcal{C}(B,C)\otimes_{\mathbb{Z}}\mathcal{C}(A,B)\to\mathcal{C}(A,C)$. Use the universal property: a homomorphism out of a tensor product is the same as a bilinear map out of the product.

> [!note]- Hint 3
> The identity morphism is a homomorphism $\mathbb{Z}\to\mathcal{C}(A,A)$; such a homomorphism is determined by where it sends $1\in\mathbb{Z}$ — that image is the identity arrow $1_A$. The unit and associativity axioms become the ordinary unit and associativity of composition, now compatible with addition.

---

# Solution

The plan: Step 1 reads off the underlying ordinary category and the group structure on hom-sets. Step 2 uses the tensor's universal property to convert enriched composition into bilinear composition. Step 3 reads off identities. Step 4 records the one-object corollary (rings).

**Step 1: The underlying category and the group structure.** An $\mathbf{Ab}$-category has objects and, for each pair, an abelian group $\mathcal{C}(A,B)$. Forgetting the group structure gives an ordinary category; remembering it equips each hom-set with addition $+$ and zero $0$.

> [!note]- Derivation
> The enriched data is: objects; hom-objects $\mathcal{C}(A,B)\in\mathbf{Ab}$ (abelian groups); composition morphisms; identity morphisms. Applying the forgetful functor $\mathbf{Ab}\to\mathbf{Set}$ (or rather $\mathbf{Ab}(\mathbb{Z},-)$, which sends a group to its underlying set) gives hom-*sets* and an ordinary category. The extra structure retained is precisely that each $\mathcal{C}(A,B)$ is an abelian group: hom-sets have a commutative, associative addition with a zero element $0_{A,B}$ and negatives.

**Step 2: Composition is bilinear.** The enriched composition morphism is a group homomorphism $c:\mathcal{C}(B,C)\otimes_{\mathbb{Z}}\mathcal{C}(A,B)\to\mathcal{C}(A,C)$; by the universal property of $\otimes_{\mathbb{Z}}$ this is the same as a $\mathbb{Z}$-bilinear map, i.e. composition distributes over addition in *both* variables.

> [!note]- Derivation
> By [[Def - Enriched Category|definition]], composition is a *morphism of $\mathcal{V}=\mathbf{Ab}$*, hence a group homomorphism $c:\mathcal{C}(B,C)\otimes_{\mathbb{Z}}\mathcal{C}(A,B)\to\mathcal{C}(A,C)$. The universal property of the tensor product (see [[Thm - Universal Property of the Tensor Product of Modules]] specialised to $\mathbb{Z}$-modules) says homomorphisms $M\otimes_{\mathbb{Z}}N\to P$ correspond bijectively to $\mathbb{Z}$-bilinear maps $M\times N\to P$. Writing $g\circ f$ for the image of $g\otimes f$, bilinearity reads
> $$(g_1+g_2)\circ f = g_1\circ f + g_2\circ f, \qquad g\circ(f_1+f_2) = g\circ f_1 + g\circ f_2,$$
> for composable $f,f_1,f_2$ and $g,g_1,g_2$. This is exactly the biadditivity of composition defining a preadditive category. (In particular $0\circ f = 0$ and $g\circ 0 = 0$, the absorbing property of the zero morphism.)

**Step 3: Identities.** The enriched identity is a homomorphism $j_A:\mathbb{Z}\to\mathcal{C}(A,A)$, determined by $j_A(1) =: 1_A$, the identity arrow; the enriched unit law becomes $1_A\circ f = f = f\circ 1_B$.

> [!note]- Derivation
> A homomorphism $j_A:\mathbb{Z}\to\mathcal{C}(A,A)$ is freely determined by the image of the generator $1\in\mathbb{Z}$, since $\mathbb{Z}$ is free on one generator; set $1_A := j_A(1)$. The enriched unit axiom, $c\circ(1\otimes j_A) = r$ and $c\circ(j_B\otimes 1)= l$, unwinds (via the unitors $\mathbb{Z}\otimes M\cong M$) to $1_A\circ f = f$ and $f\circ 1_B = f$ for $f:B\to A$ — the ordinary identity laws. Associativity of $c$ becomes ordinary associativity of composition. Hence the structure is exactly an ordinary category whose hom-sets are abelian groups with bilinear composition: a preadditive category.

**Step 4: One-object corollary — rings.** A one-object $\mathbf{Ab}$-category is a [[Def - Abelian Group|ring]]: one abelian group $R=\mathcal{C}(\star,\star)$ with bilinear multiplication (composition) and unit $1_\star$.

> [!note]- Derivation
> With a single object $\star$, the only hom-object is $R := \mathcal{C}(\star,\star)$, an abelian group under $+$. Composition is a bilinear map $R\times R\to R$ — a multiplication distributing over addition both ways — and the identity $1_\star$ is a two-sided multiplicative unit; associativity of composition is associativity of multiplication. These are precisely the axioms of a (unital, associative) ring. So "ring = one-object preadditive category", the additive analogue of "monoid = one-object category".

> [!note]- Complete formal solution
> Let $\mathcal{C}$ be enriched in $(\mathbf{Ab},\otimes_{\mathbb{Z}},\mathbb{Z})$.
>
> - *Hom-groups:* each $\mathcal{C}(A,B)$ is an abelian group; forgetting this gives an ordinary category with abelian-group hom-sets.
> - *Bilinear composition:* composition is a homomorphism $\mathcal{C}(B,C)\otimes_{\mathbb{Z}}\mathcal{C}(A,B)\to\mathcal{C}(A,C)$, equivalently (universal property of $\otimes_{\mathbb{Z}}$) a bilinear map, so $(g_1+g_2)\circ f = g_1\circ f + g_2\circ f$ and $g\circ(f_1+f_2)=g\circ f_1+g\circ f_2$.
> - *Identities and unit/associativity:* $j_A:\mathbb{Z}\to\mathcal{C}(A,A)$ gives $1_A := j_A(1)$, and the enriched unit and associativity axioms are the ordinary ones.
>
> These are exactly the axioms of a preadditive category. Conversely a preadditive category is an $\mathbf{Ab}$-category by reading composition as the homomorphism out of the tensor that the bilinear map induces. The one-object case is a ring. $\quad\blacksquare$

---

# Key Takeaways

**The choice of monoidal product, not the choice of objects, is what an enriched definition is really about.** Enriching over $\mathbf{Ab}$ would give nothing new if the monoidal product were the cartesian product $\times$ — composition would just be a function with no algebraic constraint. The entire content comes from $\otimes_{\mathbb{Z}}$: because enriched composition must be a morphism out of the *tensor*, the universal property forces bilinearity automatically. The reusable diagnostic: when you meet an enriched structure, the first question is not "what are the hom-objects?" but "what is the monoidal product, and what does a morphism out of it encode?" For $\otimes$ it is bilinearity; for $\times$ it is nothing extra.

**Bilinearity in *both* variables is forced, and forced for free, by the tensor.** A common slip is to impose additivity in one slot and check the other by hand. The tensor product makes this unnecessary: $\mathcal{C}(B,C)\otimes_{\mathbb{Z}}\mathcal{C}(A,B)$ is built precisely so that homomorphisms out of it *are* bilinear maps, with no separate verification. This is the trigger-reaction pattern to internalise — "morphism out of a tensor product" should immediately read as "bilinear map" — and it recurs everywhere from preadditive categories to algebras to the [[Thm - Tensoring is Right Exact|tensor-hom]] adjunction.

**Preadditive categories are the gateway to homological algebra, and they are one enrichment.** Adding finite biproducts to a preadditive category gives an *additive* category; adding kernels and cokernels gives an **abelian category**, the home of chain complexes, exact sequences, and derived functors. The whole tower starts here, with $\mathbf{Ab}$-enrichment. Recognising that "hom-sets are abelian groups with bilinear composition" is exactly $\mathbf{Ab}$-enrichment lets you import the general machinery of enriched category theory into homological algebra, and it is the first step toward the **stable ∞-categories** of §H.2, where the enrichment is in spectra rather than abelian groups.

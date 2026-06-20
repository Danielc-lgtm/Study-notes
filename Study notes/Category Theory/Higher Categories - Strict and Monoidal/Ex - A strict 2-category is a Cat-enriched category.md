---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Strict n-Category and Strict ω-Category"
  - "Def - 2-Category and Bicategory"
  - "Def - Enriched Category"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Prove that the following two notions coincide:

(a) a **strict $2$-category** in the globular sense — a $2$-truncated [[Def - Globular Set|globular set]] with vertical composition $\circ_1$ and horizontal composition $\circ_0$ of $2$-cells, both associative and unital, satisfying the interchange law; and

(b) a **category enriched in $\mathbf{Cat}$** — a category whose hom-sets are replaced by hom-*categories* $\mathcal{B}(A,B)$, with composition a [[Def - Functor|functor]] $\mathcal{B}(B,C)\times\mathcal{B}(A,B)\to\mathcal{B}(A,C)$ and identities chosen by functors $\mathbf{1}\to\mathcal{B}(A,A)$, subject to the enriched associativity and unit laws.

In particular, show that the [[Thm - The Interchange Law|interchange law]] in (a) is *exactly* the functoriality of the composition functor in (b), so it is not an extra axiom in the enriched picture but is automatic.

**Recall:**

A [[Def - Strict n-Category and Strict ω-Category|strict 2-category]] has $0$-cells, $1$-cells, and $2$-cells; two compositions of $2$-cells, vertical $\circ_1$ (along a shared $1$-cell) and horizontal $\circ_0$ (along a shared $0$-cell); and the interchange law $(\delta\circ_1\gamma)\circ_0(\beta\circ_1\alpha) = (\delta\circ_0\beta)\circ_1(\gamma\circ_0\alpha)$.

![[Def - Enriched Category#The Definition]]

The relevant base is $\mathcal{V} = \mathbf{Cat}$ with [[Def - Monoidal Category|monoidal]] product the cartesian product $\times$ and unit the terminal category $\mathbf{1}$ (one object, one arrow).

---

# Convergent Strategy

**Problem class:** This is an *equivalence-of-presentations* problem from the topic page's catalogue: two definitions (globular, enriched) that should describe the same objects. The work is to translate the data and axioms of each into the other and confirm they match item for item — especially the subtle correspondence "interchange = functoriality."

**Assumption pattern:** On the globular side we are given two compositions and an interchange law; on the enriched side we are given hom-categories and a composition *functor*. The unlock is that a functor between product categories is *precisely* a pair of operations (on objects = $1$-cells via $\circ_0$, on morphisms = $2$-cells via $\circ_0$) that respects the source categories' composition (= $\circ_1$) and identities — and "respects $\circ_1$" is the interchange law written out. Recognising that functoriality bundles the interchange law into a single word is the key.

**Theorem routing:** The translation routes through the [[Def - Enriched Category|definition of an enriched category]] specialized to $\mathcal{V}=\mathbf{Cat}$: a hom-object is a hom-category $\mathcal{B}(A,B)$ (its objects $=$ $1$-cells, its morphisms $=$ $2$-cells, its composition $=$ $\circ_1$); the composition morphism is a functor (which on objects is $\circ_0$ of $1$-cells, on morphisms is $\circ_0$ of $2$-cells); the enriched associativity/unit laws are equalities of functors $=$ strict associativity/unit of $\circ_0$.

**Key decision point:** The non-obvious choice is *which* composition becomes the internal structure of the hom-category and which becomes the enriched composition. Vertical composition $\circ_1$ is "inside" a single hom-category (it composes $2$-cells with a shared $1$-cell, all between fixed $0$-cells $A, B$), so it is the composition *of* $\mathcal{B}(A,B)$. Horizontal composition $\circ_0$ moves between hom-categories ($\mathcal{B}(B,C)\times\mathcal{B}(A,B)\to\mathcal{B}(A,C)$), so it is the enriched composition functor. Swapping these two roles is the natural error and produces nonsense; getting the assignment right is the crux.

---

# Legal Operations Used

1. **Operation 3 from the topic page (switch between globular and iterated-enriched definitions).** This exercise *is* operation 3 in the case $n=1$: a strict $2$-category is a category enriched in strict $1$-categories $=\mathbf{Cat}$. We use it to transfer the interchange law into functoriality and back.

2. **Operation 2 from the topic page (impose composition and check interchange).** We use the characterization of interchange as the single cross-dimensional axiom to match it against the single condition "composition is a functor."

---

# Hints

> [!note]- Hint 1
> Decide what the hom-category $\mathcal{B}(A,B)$ is: its objects should be the $1$-cells $A\to B$, and its morphisms should be the $2$-cells between them. What composition makes this a category? It must compose $2$-cells with a shared $1$-cell between the fixed $0$-cells $A, B$ — that is vertical composition $\circ_1$.

> [!note]- Hint 2
> The enriched composition is a functor $\mathcal{B}(B,C)\times\mathcal{B}(A,B)\to\mathcal{B}(A,C)$. On objects (pairs of $1$-cells) it must be horizontal composition of $1$-cells; on morphisms (pairs of $2$-cells) it must be horizontal composition $\circ_0$ of $2$-cells.

> [!note]- Hint 3
> A functor on a product category $\mathcal{X}\times\mathcal{Y}$ must (i) preserve identities and (ii) preserve composition. Write out condition (ii) for the composition functor: it says $\circ_0$ of two *vertical composites* equals the *vertical composite* of two $\circ_0$'s. Compare with the interchange law.

> [!note]- Hint 4
> Functor preserving identities, $\circ_0(1_g, 1_f) = 1_{g\circ_0 f}$, is exactly the identity-interchange axiom $1_g\circ_0 1_f = 1_{g\circ_0 f}$. The two enriched conditions (composition-preservation and identity-preservation) are precisely the two halves of "horizontal composition is a functor," which is the interchange law.

---

# Solution

The proof is a dictionary translation in both directions. Step 1 builds the enriched category from a strict $2$-category, assigning $\circ_1$ to be the internal composition of the hom-categories and $\circ_0$ to be the enriched composition functor; the interchange law is exactly what makes $\circ_0$ functorial. Step 2 runs the dictionary backwards. The single insight that does all the work is that *functoriality of a map out of a product category is interchange*.

**Step 1: From a strict $2$-category to a $\mathbf{Cat}$-enriched category.**

Define $\mathcal{B}(A,B)$ to be the category with objects the $1$-cells $f : A\to B$, morphisms the $2$-cells, and composition $\circ_1$; the enriched composition is the functor $\circ_0$, and interchange makes it a functor.

> [!note]- Derivation
> Let $\mathcal{B}$ be a strict $2$-category. For $0$-cells $A, B$, set $\mathcal{B}(A,B)$ to have:
> - objects: the $1$-cells $f : A\to B$;
> - morphisms $f\to g$: the $2$-cells $\alpha : f\Rightarrow g$;
> - composition: vertical composition $\circ_1$; identity on $f$: the degenerate $2$-cell $1_f$.
>
> This is a category: $\circ_1$ is associative and unital by the strict-$2$-category axioms. Now define the composition functor $M_{A,B,C} : \mathcal{B}(B,C)\times\mathcal{B}(A,B)\to\mathcal{B}(A,C)$ by horizontal composition: on objects $(g,f)\mapsto g\circ_0 f$, on morphisms $(\gamma,\alpha)\mapsto \gamma\circ_0\alpha$.
>
> *Is $M$ a functor?* It must preserve identities and composition in the product category $\mathcal{B}(B,C)\times\mathcal{B}(A,B)$, whose composition is *componentwise vertical*. Identity preservation: $M(1_g, 1_f) = 1_g\circ_0 1_f = 1_{g\circ_0 f}$, which is the identity-interchange axiom. Composition preservation: given $\alpha : f\Rightarrow f'$, $\beta : f'\Rightarrow f''$ in $\mathcal{B}(A,B)$ and $\gamma : g\Rightarrow g'$, $\delta : g'\Rightarrow g''$ in $\mathcal{B}(B,C)$, the product-category composite is $(\delta\circ_1\gamma, \beta\circ_1\alpha)$, and functoriality demands
> $$M(\delta\circ_1\gamma,\, \beta\circ_1\alpha) = M(\delta,\gamma)\circ_1 M(\gamma\dots)\dots,$$
> precisely $(\delta\circ_1\gamma)\circ_0(\beta\circ_1\alpha) = (\delta\circ_0\beta)\circ_1(\gamma\circ_0\alpha)$ — the [[Thm - The Interchange Law|interchange law]]. So $M$ is a functor *exactly because* interchange holds. The identity $1_A$ is selected by the functor $\mathbf{1}\to\mathcal{B}(A,A)$ picking out the degenerate $1$-cell $1_A$. Strict associativity and unit of $\circ_0$ are the enriched associativity and unit laws (equalities of functors). Hence $\mathcal{B}$ is a $\mathbf{Cat}$-enriched category.

**Step 2: From a $\mathbf{Cat}$-enriched category to a strict $2$-category.**

> [!note]- Derivation
> Let $\mathcal{B}$ be enriched in $(\mathbf{Cat},\times,\mathbf{1})$. Read off:
> - $0$-cells: the objects of $\mathcal{B}$;
> - $1$-cells $A\to B$: the *objects* of the hom-category $\mathcal{B}(A,B)$;
> - $2$-cells: the *morphisms* of $\mathcal{B}(A,B)$;
> - vertical composition $\circ_1$: composition *inside* the category $\mathcal{B}(A,B)$ (associative and unital because $\mathcal{B}(A,B)$ is a category);
> - horizontal composition $\circ_0$: the action of the composition functor $M_{A,B,C}$ on objects (for $1$-cells) and on morphisms (for $2$-cells);
> - degenerate $2$-cells $1_f$: identity morphisms in $\mathcal{B}(A,B)$; identity $1$-cells $1_A$: the object selected by $\mathbf{1}\to\mathcal{B}(A,A)$.
>
> The globularity equations hold by construction (a $2$-cell's source and target are parallel $1$-cells, i.e. objects of the same hom-category). Strict associativity and unit of $\circ_0$ are the enriched associativity/unit laws. The interchange law holds because $M$ is a functor: functoriality on the product category $\mathcal{B}(B,C)\times\mathcal{B}(A,B)$ is, written componentwise, exactly $(\delta\circ_1\gamma)\circ_0(\beta\circ_1\alpha) = (\delta\circ_0\beta)\circ_1(\gamma\circ_0\alpha)$, and $M(1_g,1_f)=1_{g\circ_0 f}$. So $\mathcal{B}$ is a strict $2$-category. The two constructions are mutually inverse, since each reads off the same underlying data.

> [!note]- Complete formal solution
> Fix the base $(\mathbf{Cat},\times,\mathbf{1})$.
>
> **($a\Rightarrow b$)** From a strict $2$-category $\mathcal{B}$, define $\mathcal{B}(A,B)$ to have objects the $1$-cells $A\to B$, morphisms the $2$-cells, and composition $\circ_1$; it is a category by the strict axioms for $\circ_1$. Define $M_{A,B,C}=\circ_0 : \mathcal{B}(B,C)\times\mathcal{B}(A,B)\to\mathcal{B}(A,C)$ on objects and morphisms by horizontal composition. Then $M$ is a functor iff it preserves identities ($1_g\circ_0 1_f=1_{g\circ_0 f}$) and composition ($(\delta\circ_1\gamma)\circ_0(\beta\circ_1\alpha)=(\delta\circ_0\beta)\circ_1(\gamma\circ_0\alpha)$), which are exactly the identity-interchange and interchange axioms. The unit functors $\mathbf{1}\to\mathcal{B}(A,A)$ pick out $1_A$; enriched associativity/unit are strict associativity/unit of $\circ_0$. So $\mathcal{B}$ is $\mathbf{Cat}$-enriched.
>
> **($b\Rightarrow a$)** From a $\mathbf{Cat}$-enriched category, take $0$-cells $=$ objects, $1$-cells $=$ objects of hom-categories, $2$-cells $=$ morphisms of hom-categories, $\circ_1 =$ hom-category composition, $\circ_0 =$ composition functor on objects/morphisms, identities as the selected ones. Globularity holds by construction; strict associativity/unit of $\circ_0$ are the enriched laws; interchange and identity-interchange are functoriality of $M$. So this is a strict $2$-category.
>
> The constructions are mutually inverse, so the two notions coincide, and the [[Thm - The Interchange Law|interchange law]] is precisely the functoriality of the enriched composition. $\qquad\blacksquare$

---

# Key Takeaways

**Interchange is not an extra axiom — it is functoriality in disguise, and that is why iterated enrichment is the right inductive definition.** The central lesson is that the apparently mysterious interchange law, which in the globular presentation must be imposed by hand as a separate cross-dimensional compatibility, becomes *automatic* in the enriched presentation: it is nothing but the statement that the composition functor is a functor on a product category. This is the payoff of the iterated-enrichment definition of strict $n$-categories ($n$-category $=$ category enriched in $(n-1)$-categories): each new level's interchange comes free with functoriality, so the whole tower of interchange laws is generated by a single inductive idea rather than an ever-growing list of axioms. Whenever you meet a cross-dimensional compatibility in a higher structure, ask whether it is the functoriality of some composition — it usually is.

**Vertical composition lives inside a hom-object; horizontal composition moves between hom-objects.** The key decision in the proof — which composition becomes internal and which becomes enriched — encodes a general principle about higher categories. Composition along a *high*-dimensional boundary (vertical, $\circ_1$) keeps you within a single hom-category and is therefore part of that hom-object's internal structure. Composition along a *low*-dimensional boundary (horizontal, $\circ_0$) carries you across hom-objects and is therefore the enriched composition functor. This pattern persists up the dimensions: in a strict $n$-category, the top composition is internal to the top-level hom-objects, and the lower compositions are successively more "external." Keeping straight which boundary a composition glues along tells you immediately where it sits in the enriched picture.

**Choosing the right base of enrichment converts higher-categorical questions into ordinary categorical ones.** By recognising a strict $2$-category as a $\mathbf{Cat}$-enriched category, every theorem about [[Def - Enriched Category|enriched categories]] — enriched functors, enriched natural transformations, enriched (co)limits, the enriched Yoneda lemma — instantly applies to $2$-categories with no separate development. This is the same leverage seen in part (a) of the companion exercise on globular sets as presheaves: identify your exotic structure as an instance of a well-developed general framework (enrichment here, presheaves there) and inherit its entire theory. The trigger to internalise: when defining functors, transformations, or limits in a higher-categorical setting, first ask "enriched in what?" — the answer routes you to an existing body of theory rather than forcing you to reinvent it.

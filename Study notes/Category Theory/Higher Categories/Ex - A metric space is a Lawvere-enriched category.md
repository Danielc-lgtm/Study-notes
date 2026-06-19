---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Enriched Category"
  - "Def - Monoidal Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{V} = ([0,\infty], \geq, +, 0)$ be the extended non-negative reals, regarded as a [[Def - Monoidal Category|monoidal category]]: objects are the numbers in $[0,\infty]$, there is a unique morphism $x \to y$ exactly when $x \geq y$, the monoidal product is $\otimes = +$ (addition), and the unit is $I = 0$. Show that a category enriched in $\mathcal{V}$ is precisely a **(generalised) metric space** in Lawvere's sense:

1. The objects are the points; the hom-object $\mathcal{C}(a,b) \in [0,\infty]$ is the distance $d(a,b)$.
2. The enriched composition morphism is the **triangle inequality** $d(b,c) + d(a,b) \geq d(a,c)$.
3. The enriched identity morphism is $d(a,a) = 0$.

Explain which axioms of a *classical* metric space (symmetry, finiteness, $d(a,b)=0\Rightarrow a=b$) are *dropped* in this correspondence, and why dropping them is natural from the enriched viewpoint.

**Recall:**

![[Def - Enriched Category#The Definition]]

A [[Def - Monoidal Category|monoidal category]] needs a product $\otimes$, a unit $I$, and coherent associativity/unit isomorphisms. Here $\mathcal{V}$ is a *poset* (at most one morphism between any two objects), so all coherence diagrams commute automatically. A morphism $x \to y$ exists iff $x \geq y$.

---

# Convergent Strategy

**Problem class:** This is the marquee "identification by unwinding" of the chapter, where the unwound structure is startlingly far from a category. The routine is still mechanical — substitute $\mathcal{V}=([0,\infty],\geq,+)$ into [[Def - Enriched Category|the enriched definition]] — but the payoff is that a metric space and a category turn out to be one definition.

**Assumption pattern:** The recognisable features are three properties of $\mathcal{V}$: its morphisms are the *reversed* order $\geq$ (so "a morphism exists" means "is at least"), its product is $+$, and its unit is $0$. Each of these maps onto one piece of metric-space data: distances are hom-objects, the triangle inequality is composition, and zero self-distance is the identity.

**Theorem routing:** No external theorem is needed; the route is purely Legal Operation 1 (unwind in the base), made delicate by the fact that $\mathcal{V}$ is a poset, so every "axiom" of the enriched category is automatically satisfied as soon as the relevant inequality holds — there is nothing to check beyond the inequalities themselves.

**Key decision point:** The non-obvious choice is the *reversed* order $\geq$ as the morphisms of $\mathcal{V}$. Using the usual order $\leq$ would make composition read $d(b,c)+d(a,b)\leq d(a,c)$ — the *wrong* direction. The whole correspondence hinges on orienting $\mathcal{V}$ so that "there is a morphism $x\to y$" means "$x\geq y$", because then "composition exists" forces the triangle inequality in the correct direction.

---

# Legal Operations Used

1. **Operation 1 (unwind an enriched definition in the base).** We substitute $\mathcal{V}=([0,\infty],\geq,+,0)$ and translate hom-objects, composition, and identities into distances, the triangle inequality, and zero self-distance.

---

# Hints

> [!note]- Hint 1
> In a poset viewed as a category, "there is a morphism $x\to y$" is just the proposition "$x\geq y$". So an *equation between morphisms* is automatic (posets have at most one arrow), and the only content of any enriched axiom is *whether the required morphism exists* — i.e. whether an inequality holds.

> [!note]- Hint 2
> The composition morphism has type $\mathcal{C}(b,c)\otimes\mathcal{C}(a,b)\to\mathcal{C}(a,c)$. With $\otimes=+$ and a morphism meaning $\geq$, this morphism *exists* iff $\mathcal{C}(b,c)+\mathcal{C}(a,b)\geq\mathcal{C}(a,c)$. Now read $\mathcal{C}(a,b)=d(a,b)$.

> [!note]- Hint 3
> The identity morphism has type $I\to\mathcal{C}(a,a)$, i.e. $0\to d(a,a)$, which exists iff $0\geq d(a,a)$, forcing $d(a,a)=0$. Which classical metric axioms have you *not* used? Symmetry ($d(a,b)=d(b,a)$) and the separation axiom ($d=0\Rightarrow$ equal) never appeared.

---

# Solution

The plan: Step 1 records that $\mathcal{V}$ is a monoidal poset so all axioms reduce to inequalities. Step 2 reads hom-objects as distances. Step 3 reads composition as the triangle inequality. Step 4 reads identities as $d(a,a)=0$ and identifies the dropped classical axioms.

**Step 1: $\mathcal{V}$ is a monoidal poset; all enriched axioms are inequalities.** Because $\mathcal{V}=([0,\infty],\geq)$ has at most one morphism between any two objects, every diagram in $\mathcal{V}$ commutes automatically, so the *only* content of an enriched axiom is the existence of certain morphisms — i.e. certain inequalities.

> [!note]- Derivation
> $([0,\infty],\geq)$ is a poset, hence a category with at most one arrow $x\to y$ (present iff $x\geq y$). Two parallel morphisms are automatically equal, so associativity and unit axioms — which are *equations between morphisms* — hold vacuously whenever the morphisms exist. The product $+$ is associative and unital ($x+0=x$) and monotone, so $([0,\infty],\geq,+,0)$ is a (strict) monoidal poset. Thus enriching over $\mathcal{V}$ has *no* equational content; all that can be required is that prescribed morphisms exist.

**Step 2: Hom-objects are distances.** A hom-object $\mathcal{C}(a,b)\in[0,\infty]$ is a number; set $d(a,b):=\mathcal{C}(a,b)$.

> [!note]- Derivation
> By [[Def - Enriched Category|definition]], for each ordered pair of objects $a,b$ there is a hom-object $\mathcal{C}(a,b)$, an *object of $\mathcal{V}$*, i.e. an element of $[0,\infty]$. Calling the objects "points" and $\mathcal{C}(a,b)$ "the distance $d(a,b)$" is just renaming. Note the distance is directed: $d(a,b)$ and $d(b,a)$ are unrelated, because $\mathcal{C}(a,b)$ and $\mathcal{C}(b,a)$ are independent hom-objects.

**Step 3: Composition is the triangle inequality.** The composition morphism $\mathcal{C}(b,c)\otimes\mathcal{C}(a,b)\to\mathcal{C}(a,c)$, with $\otimes=+$ and a morphism meaning $\geq$, exists iff $d(b,c)+d(a,b)\geq d(a,c)$ — the triangle inequality.

> [!note]- Derivation
> The required composition morphism is an arrow $\mathcal{C}(b,c)\otimes\mathcal{C}(a,b)\to\mathcal{C}(a,c)$ in $\mathcal{V}$. Since $\otimes=+$, the source is the number $\mathcal{C}(b,c)+\mathcal{C}(a,b) = d(b,c)+d(a,b)$, and the target is $\mathcal{C}(a,c)=d(a,c)$. A morphism $x\to y$ exists iff $x\geq y$, so the composition morphism exists for all $a,b,c$ iff
> $$d(b,c)+d(a,b)\geq d(a,c)\qquad\text{for all } a,b,c.$$
> This is exactly the triangle inequality. So "composition is defined" *is* the triangle inequality — composition in the enriched category literally *is* the triangle inequality, with the additivity $\otimes=+$ supplying the "$+$" and the order supplying the "$\geq$".

**Step 4: Identities are $d(a,a)=0$; dropped axioms.** The identity morphism $I\to\mathcal{C}(a,a)$, i.e. $0\geq d(a,a)$, forces $d(a,a)=0$. Symmetry, finiteness, and separation are *not* required.

> [!note]- Derivation
> The enriched identity is a morphism $j_a:I\to\mathcal{C}(a,a)$, i.e. $0\to d(a,a)$, which exists iff $0\geq d(a,a)$; since $d(a,a)\geq 0$ always, this forces $d(a,a)=0$. That is the only identity content. Now observe what was *never* used:
> - **Symmetry** $d(a,b)=d(b,a)$: never required, because $\mathcal{C}(a,b)$ and $\mathcal{C}(b,a)$ are independent hom-objects. Enriched categories are inherently *directed* (just as ordinary categories have directed morphisms), so the natural notion is an *asymmetric* (quasi-)metric.
> - **Finiteness**: $d(a,b)=\infty$ is allowed, because $\infty\in[0,\infty]$ is a legitimate object of $\mathcal{V}$. Infinite distances correspond to "no morphism of finite cost", entirely natural.
> - **Separation** $d(a,b)=0\Rightarrow a=b$: never required, because distinct objects may have a zero hom-object — this is the categorical analogue of distinct objects being isomorphic. A *skeletal* enriched category would impose it.
>
> So an $\mathcal{V}$-category is a **generalised (Lawvere) metric space**: a set with a directed, possibly-infinite distance satisfying $d(a,a)=0$ and the triangle inequality. Imposing symmetry, finiteness, and separation recovers the classical notion.

> [!note]- Complete formal solution
> Let $\mathcal{C}$ be enriched in $\mathcal{V}=([0,\infty],\geq,+,0)$.
>
> - $\mathcal{V}$ is a monoidal poset, so all enriched axioms reduce to the existence of morphisms, i.e. to inequalities (Step 1).
> - Objects are points; $d(a,b):=\mathcal{C}(a,b)\in[0,\infty]$ (Step 2).
> - Composition exists iff $d(b,c)+d(a,b)\geq d(a,c)$ for all $a,b,c$ — the triangle inequality (Step 3).
> - The identity exists iff $0\geq d(a,a)$, i.e. $d(a,a)=0$ (Step 4).
>
> Thus a $\mathcal{V}$-category is exactly a set with a function $d:X\times X\to[0,\infty]$ satisfying $d(a,a)=0$ and the triangle inequality: a generalised metric space. Symmetry, finiteness, and the separation axiom are not part of the enriched structure; adding them recovers the classical metric space. $\quad\blacksquare$

---

# Key Takeaways

**Enrichment shows that "metric space" and "category" are the *same* concept over different bases — the deepest single instance of the enrichment idea.** A category is enrichment over $\mathbf{Set}$; a metric space is enrichment over $([0,\infty],\geq,+)$. Composition of morphisms and the triangle inequality are the *same axiom*, read in two monoidal categories. The reusable lesson is that the enriched-category axioms are extraordinarily flexible: by choosing the base $\mathcal{V}$ you can make "category" mean a metric space, a preadditive category, a $2$-category, or a simplicial category. When you meet a structure with a "composition-like" law (triangle inequality, transitivity, subadditivity), ask whether it is enrichment over a cleverly chosen $\mathcal{V}$.

**In a poset base, all content is in the inequalities — equational axioms evaporate.** Because $([0,\infty],\geq)$ has at most one morphism between objects, associativity and the unit law of the enriched category are automatically satisfied; the *only* thing to check is whether the required morphisms exist, which is whether the triangle inequality and $d(a,a)=0$ hold. This is a general and labour-saving phenomenon: enriching over a *poset* turns a category-theoretic structure into a *relational* one (preorders, metric spaces, closure operators), where the higher coherence is free. Recognising "the base is a poset" tells you immediately that there are no commuting-diagram obligations, only inequalities.

**The axioms a correspondence *omits* are as informative as those it includes — and they predict the right generalisation.** Classical metric spaces demand symmetry, finiteness, and separation; the enriched viewpoint demands none of them, and each omission is *natural*. Directedness (no symmetry) is intrinsic to categories, where morphisms have a direction. Infinite distances are fine because $\infty$ is a perfectly good object. Non-separation mirrors distinct-but-isomorphic objects. So Lawvere's definition does not "forget" axioms by accident — it reveals that symmetry and separation were never the categorical core, and that the natural objects are *quasi-metric* spaces (asymmetric, used in computer science for cost models and in analysis for one-sided distances). Whenever an abstract framework drops a familiar axiom, the lesson is to ask what the framework is telling you about which axioms are essential and which were conveniences.

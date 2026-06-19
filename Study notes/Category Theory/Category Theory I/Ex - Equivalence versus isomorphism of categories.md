---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Equivalence of Categories"
  - "Def - Functor"
  - "Def - Natural Transformation"
tags: [category-theory, foundations]
---

# Problem Statement

Pin down the difference between [[Def - Equivalence of Categories|equivalence]] and **isomorphism** of categories.

1. Show every isomorphism of categories is an equivalence.
2. Give an explicit equivalence that is **not** an isomorphism: let $\mathbf{1}$ be the [[Def - Category|terminal category]] (one object, one morphism) and let $\mathcal{C}$ be the "walking isomorphism" $\mathcal{I}$ — two objects $a, b$ with a unique isomorphism between them in each direction (so $\mathcal{I}(a,a) = \{1_a\}$, $\mathcal{I}(a,b) = \{f\}$, $\mathcal{I}(b,a) = \{f^{-1}\}$, $\mathcal{I}(b,b) = \{1_b\}$). Show $\mathbf{1} \simeq \mathcal{I}$ but $\mathbf{1} \not\cong \mathcal{I}$.
3. Conclude: an isomorphism demands $GF = 1$ and $FG = 1$ *on the nose*; an equivalence only demands $GF \cong 1$ and $FG \cong 1$ up to natural isomorphism — and the second condition is the right one because it respects "objects only matter up to iso".

**Recall:**

![[Def - Equivalence of Categories#The Definition]]

An [[Def - Equivalence of Categories|equivalence]] is data $(F, G, \eta, \varepsilon)$ with natural isomorphisms $\eta : 1_{\mathcal{C}} \cong GF$, $\varepsilon : FG \cong 1_{\mathcal{D}}$. An isomorphism of categories requires $GF = 1_{\mathcal{C}}$ and $FG = 1_{\mathcal{D}}$ as equalities.

---

# Convergent Strategy

**Problem class:** This is a "separate two notions and exhibit the gap with a minimal example" exercise. The route is: prove the easy implication, then build the smallest equivalence-that-is-not-an-isomorphism, locating the gap in object-count.

**Assumption pattern:** Isomorphism demands equality of the round-trip composites with the identity; equivalence only demands natural isomorphism. The minimal place this gap appears is when the two categories have different numbers of objects but the "same" structure up to iso — exactly $\mathbf{1}$ (one object) versus $\mathcal{I}$ (two isomorphic objects).

**Theorem routing:** (1) is immediate: equalities are in particular natural isomorphisms. (2) builds functors $F : \mathbf{1} \to \mathcal{I}$ and $G : \mathcal{I} \to \mathbf{1}$ and checks $GF = 1_{\mathbf{1}}$ exactly but $FG \cong 1_{\mathcal{I}}$ only up to natural iso (not equality), then rules out isomorphism by counting objects.

**Key decision point:** The instructive choice is the example $\mathcal{I}$: it has two *isomorphic* objects, so collapsing it to $\mathbf{1}$ loses no structure up to iso, but the collapse cannot be an equality (the round trip $\mathbf{1} \to \mathcal{I} \to \mathbf{1}$ vs $\mathcal{I} \to \mathbf{1} \to \mathcal{I}$ sends $b$ to $a$, not to $b$). Seeing that the obstruction to equality is "the round trip moves an object to its isomorphic partner" is the crux.

---

# Legal Operations Used

1. **Operation: weaken equality to natural isomorphism** (topic page, Legal Operation 11). Every equality of functors is a natural isomorphism, giving (1).

2. **Operation: build a minimal counterexample category** (topic page, Legal Operation 1). $\mathcal{I}$, the walking isomorphism, is the smallest witness.

3. **Operation: refute isomorphism by object-count** (topic page, Legal Operation 3). $\mathbf{1}$ has one object, $\mathcal{I}$ has two.

---

# Hints

> [!note]- Hint 1
> If $GF = 1_{\mathcal{C}}$ as functors, is the identity natural transformation $1_{\mathcal{C}} \Rightarrow GF$ a natural isomorphism? (Equality is the strongest form of natural isomorphism.)

> [!note]- Hint 2
> For $\mathbf{1} \simeq \mathcal{I}$: define $F : \mathbf{1} \to \mathcal{I}$ sending the unique object to $a$, and $G : \mathcal{I} \to \mathbf{1}$ sending both $a, b$ to the unique object. Compute $GF$ and $FG$.

> [!note]- Hint 3
> $GF = 1_{\mathbf{1}}$ exactly. But $FG$ sends $a \mapsto a$ and $b \mapsto a$ — it is *not* $1_{\mathcal{I}}$ (which would fix $b$). Is $FG \cong 1_{\mathcal{I}}$ via a natural isomorphism using the iso $f : a \to b$?

> [!note]- Hint 4
> Not isomorphic: an isomorphism of categories is a bijection on objects. $\mathbf{1}$ has one object, $\mathcal{I}$ has two. Done.

---

# Solution

The plan: equality implies natural isomorphism, so isomorphisms are equivalences (part 1). Then build $F, G$ between $\mathbf{1}$ and $\mathcal{I}$ with $GF = 1$ but $FG$ only naturally isomorphic to $1$, witnessing equivalence without isomorphism (part 2). The object-count rules out isomorphism, and the analysis isolates the $=$-versus-$\cong$ gap (part 3).

**Step 1: Isomorphisms are equivalences.**

> [!note]- Derivation
> Suppose $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ satisfy $GF = 1_{\mathcal{C}}$ and $FG = 1_{\mathcal{D}}$ (an isomorphism of categories). Take $\eta = 1_{1_{\mathcal{C}}}$ (the identity natural transformation on $1_{\mathcal{C}}$, which equals $GF$) and $\varepsilon = 1_{1_{\mathcal{D}}}$. An identity natural transformation is a [[Def - Natural Transformation|natural isomorphism]] (every component is an identity, hence an iso). So $(F, G, \eta, \varepsilon)$ is an [[Def - Equivalence of Categories|equivalence]]. Hence every isomorphism of categories is an equivalence.

**Step 2: An equivalence that is not an isomorphism.**

> [!note]- Derivation
> Let $\mathbf{1} = \{\ast\}$ (one object, only $1_\ast$) and $\mathcal{I}$ the walking isomorphism: objects $a, b$, a unique iso $f : a \to b$ with inverse $f^{-1} : b \to a$, and the two identities. Define $F : \mathbf{1} \to \mathcal{I}$ by $F(\ast) = a$ (and $F(1_\ast) = 1_a$), and $G : \mathcal{I} \to \mathbf{1}$ by $G(a) = G(b) = \ast$ (and every morphism of $\mathcal{I}$ to $1_\ast$). Both are functors.
>
> *Round trip $GF$:* $GF(\ast) = G(a) = \ast$ and $GF(1_\ast) = 1_\ast$, so $GF = 1_{\mathbf{1}}$ *on the nose*.
>
> *Round trip $FG$:* $FG(a) = F(\ast) = a$ but $FG(b) = F(\ast) = a \neq b$. So $FG \neq 1_{\mathcal{I}}$ as functors. However $FG \cong 1_{\mathcal{I}}$ via the natural isomorphism $\varepsilon : FG \Rightarrow 1_{\mathcal{I}}$ with components $\varepsilon_a = 1_a : a \to a$ and $\varepsilon_b = f^{-1} : a \to b$? Let us check: we need $\varepsilon_x : FG(x) \to x$, so $\varepsilon_a : a \to a$ is $1_a$ and $\varepsilon_b : a \to b$ is $f$. Naturality for the morphism $f : a \to b$ requires $1_{\mathcal{I}}(f) \circ \varepsilon_a = \varepsilon_b \circ FG(f)$, i.e. $f \circ 1_a = f \circ FG(f)$; since $FG(f) = 1_a$ (everything in $\mathcal{I}$ goes to $\ast$ and back to $1_a$), both sides are $f$. So the square commutes, each component is an iso, and $\varepsilon : FG \xRightarrow{\sim} 1_{\mathcal{I}}$. Thus $(F, G, 1, \varepsilon)$ is an [[Def - Equivalence of Categories|equivalence]], and $\mathbf{1} \simeq \mathcal{I}$.

**Step 3: Not an isomorphism, and the moral.**

> [!note]- Derivation
> An [[Def - Equivalence of Categories|isomorphism of categories]] requires a bijection on object-collections. But $\mathbf{1}$ has *one* object and $\mathcal{I}$ has *two*, so no bijection exists: $\mathbf{1} \not\cong \mathcal{I}$. The obstruction to isomorphism is precisely that $FG$ moves $b$ to its isomorphic partner $a$ rather than fixing it — equality $FG = 1$ would forbid this, while natural isomorphism $FG \cong 1$ permits it (the iso $f : a \to b$ supplies the natural comparison). This is the entire difference: **isomorphism freezes objects in place; equivalence allows the round trip to land on an isomorphic object, with a natural iso recording the displacement.** The latter is the right notion because categorically $a$ and $b$, being isomorphic, are indistinguishable, so demanding the round trip return to $b$ *on the nose* is meaningless overspecification.

> [!note]- Complete formal solution
> *(1)* If $GF = 1_{\mathcal{C}}$, $FG = 1_{\mathcal{D}}$, take $\eta, \varepsilon$ to be identity natural transformations (natural isos), giving an equivalence.
>
> *(2)* $F : \mathbf{1} \to \mathcal{I}$, $\ast \mapsto a$; $G : \mathcal{I} \to \mathbf{1}$, $a, b \mapsto \ast$. Then $GF = 1_{\mathbf{1}}$ exactly, and $FG \cong 1_{\mathcal{I}}$ via $\varepsilon_a = 1_a$, $\varepsilon_b = f$ (naturality checks out, components are isos). So $\mathbf{1} \simeq \mathcal{I}$.
>
> *(3)* No object-bijection $\mathbf{1} \leftrightarrow \mathcal{I}$ exists (one vs two objects), so $\mathbf{1} \not\cong \mathcal{I}$. Equivalence weakens $FG = 1$ to $FG \cong 1$, which is the correct notion since isomorphic objects are categorically indistinguishable. $\blacksquare$

---

# Key Takeaways

**Equivalence weakens equality of round-trips to natural isomorphism — and that weakening is the whole point.** The structural lesson is that the only difference between isomorphism and equivalence of categories is whether $GF = 1$ and $FG = 1$ are demanded *as equalities* or merely *up to natural isomorphism*. Isomorphism is almost always the wrong notion because it can see the multiplicity of isomorphic objects, which categorical reasoning declares irrelevant. The trigger to prefer equivalence: any time you would say "these two categories are the same", check whether you really mean "the same up to relabelling isomorphic objects" — you almost always do, and that is equivalence, not isomorphism.

**The gap lives in object-count: equivalent categories can have different numbers of objects.** The minimal witness $\mathbf{1} \simeq \mathcal{I}$ shows the cleanest manifestation of the gap: $\mathcal{I}$ has a redundant second object isomorphic to the first, and equivalence collapses the redundancy while isomorphism cannot. This generalizes to $\mathbf{FinVect}_k \simeq \mathbf{Mat}_k$ and to every "category versus its skeleton". The diagnostic for "equivalent but not isomorphic" is exactly an object-count mismatch arising from isomorphic copies; if the object-collections have different cardinalities yet the same iso-class structure, you have an equivalence that is not an isomorphism.

**Isomorphic objects are categorically indistinguishable, so freezing them is meaningless.** The deepest takeaway is the principle behind the definition: in a category, an object is only ever known up to isomorphism, so a notion of sameness (equivalence) that allows the round trip $FG$ to land on an isomorphic object — rather than the literal object — is the one respecting the category's own standards. Demanding $FG = 1$ on the nose imposes a distinction (this object versus that isomorphic object) that the category itself refuses to make. This is the same principle that, pushed further, becomes the univalence axiom of homotopy type theory: isomorphic objects should be interchangeable, and equivalence is its first incarnation.

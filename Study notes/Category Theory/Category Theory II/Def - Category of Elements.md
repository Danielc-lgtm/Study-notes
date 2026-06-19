---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Presheaf"
  - "Def - Universal Element"
  - "Def - Initial and Terminal Object"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a small (or locally small) category and $F : \mathcal{C}^{op} \to \mathbf{Set}$ a [[Def - Presheaf|presheaf]] (the covariant case is the dual). The **category of elements** is written $\int_{\mathcal{C}} F$, or $\int F$, or $\mathrm{El}(F)$, or $\mathcal{C}/F$; all are synonyms. Its objects are pairs $(A, x)$ with $x \in F(A)$. There is a canonical forgetful (projection) functor $\pi : \int F \to \mathcal{C}$, $(A, x) \mapsto A$. The full registry is on [[Category Theory II — Universal Properties, Representability, and the Yoneda Lemma]].

---

# Axiom Motivation

We have repeatedly said that a universal property is "being initial or terminal in a category of candidates" (see [[Def - Universal Property and Universal Arrow]]), and that a [[Def - Universal Element|universal element]] is "the generic element from which all others derive". The category of elements is the construction that makes both slogans literally true at once: it is the precise category in which the universal element sits as an initial or terminal object. Without it, "universal" is a family of analogies; with it, "universal" is a synonym for "initial or terminal", uniformly.

The construction is forced by what we want it to do. We want objects to be "elements of $F$" — pairs $(A, x)$ with $x \in F(A)$, since an element of a set-valued functor is exactly an object together with an element of the set it sits over. We want morphisms to record *how one element restricts to another*. For a presheaf, $F$ acts contravariantly: a morphism $f : B \to A$ gives a restriction $F(f) : F(A) \to F(B)$. So the natural notion of a morphism $(B, x) \to (A, u)$ is a map $f : B \to A$ whose restriction carries $u$ down to $x$, that is $F(f)(u) = x$. With this choice, the universal-element condition "for every $(B, x)$ there is a unique $f$ with $F(f)(u) = x$" becomes verbatim "there is a unique morphism $(B, x) \to (A, u)$" — which is terminality of $(A, u)$. The construction is engineered so that the universal element is terminal.

Why orient the morphisms toward $A$ rather than away? Because we insisted (following Riehl's convention) that the forgetful functor $\pi : \int F \to \mathcal{C}$ should be well-defined for both variances, and because we want the universal element to be the place *everything flows to*. For a contravariant $F$ the universal element is terminal and arrows point toward it; for a covariant $F$ the same construction makes the universal element initial and arrows point away from it. The variance of $F$ controls the variance of universality — and the category of elements is precisely the gadget that converts the one into the other. This is the structural insight that closes the chapter: every universal property is an initial/terminal object, in $\int F$.

There is a second, equally important use. The category of elements provides a *representability test*. To decide whether a given set-valued functor $F$ is representable, build $\int F$ and ask: does it have a terminal object? If yes, that terminal object *is* the universal element and yields the representation; if no, $F$ is not representable. This converts an existential question about natural isomorphisms into a search for a terminal object, which is often decidable by inspection.

---

# The Definition

Let $F : \mathcal{C}^{op} \to \mathbf{Set}$ be a presheaf.

The **category of elements** $\int F$ has:
- **objects** the elements of $F$: pairs $(A, x)$ where $A \in \mathcal{C}$ and $x \in F(A)$;
- **morphisms** $(B, x) \to (A, u)$ the morphisms $f : B \to A$ in $\mathcal{C}$ such that $F(f)(u) = x$ (the restriction of $u$ along $f$ is $x$);
- composition and identities inherited from $\mathcal{C}$ (one checks the defining condition is preserved by composition, using functoriality of $F$).

It comes equipped with the **projection functor** $\pi : \int F \to \mathcal{C}$, $(A, x) \mapsto A$, $f \mapsto f$, which simply forgets the chosen element.

For a covariant functor $F : \mathcal{C} \to \mathbf{Set}$, the category of elements $\int F$ has the same objects, but a morphism $(A, x) \to (B, y)$ is a map $f : A \to B$ with $F(f)(x) = y$; the projection $\pi : \int F \to \mathcal{C}$ is again the forgetful functor.

This is the **Grothendieck construction** applied to a $\mathbf{Set}$-valued functor.

---

# Categorical / Structural Definition

The category of elements is a **comma category** in disguise. For $F : \mathcal{C}^{op} \to \mathbf{Set}$, regard $F$ as an object of the presheaf category $[\mathcal{C}^{op}, \mathbf{Set}]$ and let $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$ be the [[Def - The Yoneda Embedding|Yoneda embedding]]. Then
$$\int F \;\cong\; (\mathbf{y} \downarrow F),$$
the comma category whose objects are pairs $(A, \alpha)$ with $\alpha : \mathbf{y}A \Rightarrow F$ a natural transformation. The isomorphism is the [[Thm - The Yoneda Lemma|Yoneda lemma]]: a natural transformation $\mathbf{y}A = \mathcal{C}(-, A) \Rightarrow F$ is the same as an element $x \in F(A)$. So "object of $\int F$" = "element of $F$" = "natural transformation from a representable into $F$", and the three descriptions agree on morphisms too.

The structural theorem this makes possible is the equivalence at the heart of §2.4:

> **$F$ is [[Def - Hom-Functor and Representable Functor|representable]] $\iff$ $\int F$ has a terminal object (contravariant case) or an initial object (covariant case), and that object is the [[Def - Universal Element|universal element]].**

This is the content of [[Thm - Uniqueness of Universal Objects]] and Riehl's Proposition 2.4.8. It is the precise statement that *universal = initial or terminal*.

---

# Relate to Other Fields / Compression

The category of elements unifies a long list of familiar "categories of structured objects" as instances of $\int F$ for the right $F$. The category of **pointed objects** in a concrete category $\mathcal{C}$ is $\int U$ for the forgetful functor $U : \mathcal{C} \to \mathbf{Set}$ — an object plus a chosen point. The category of **$n$-colored graphs** is $\int F$ for the $n$-coloring functor on graphs. The category of **discrete dynamical systems** is $\int U$ for the forgetful functor from sets-with-an-endomorphism. The **translation groupoid** of a group action is the category of elements of the corresponding $G$-set. In each case the morphisms are "structure-preserving maps that respect the chosen element", which is exactly the $F(f)(u) = x$ condition.

**True name:** the category of elements is *the category of (object, element) pairs with restriction-respecting maps*; equivalently, the comma category $(\mathbf{y} \downarrow F)$. The operational payoff: it turns "is $F$ representable?" into "does $\int F$ have a terminal object?", and it turns the universal element into a terminal object you can recognize on sight.

---

# Examples / Corollaries

**Is an instance — the slice category as $\int \mathcal{C}(-, A)$.** Take $F = \mathcal{C}(-, A)$, the representable presheaf of $A$. An element of $F$ is a morphism $f : B \to A$, so $\int F$ is the **slice category** $\mathcal{C}/A$ of objects-over-$A$. Its terminal object is $(A, 1_A)$ — the identity — which is exactly the universal element, confirming that representable functors have universal elements. Drilled at [[Ex - The category of elements of a representable functor]].

**Is an instance — the category of pointed sets.** For the identity functor $\mathrm{id} : \mathbf{Set} \to \mathbf{Set}$ (which is the forgetful functor on $\mathbf{Set}$), $\int \mathrm{id}$ is the category of **pointed sets**: objects are pairs $(X, x_0)$ of a set with a chosen basepoint, morphisms are basepoint-preserving functions. The identity functor is representable by the one-point set $*$ (since $\mathbf{Set}(*, X) \cong X$), and the universal element is the unique point of $*$, which is the initial object of $\int \mathrm{id}$ — the one-point pointed set.

> [!note]- Algebraic geometry background: representability via a terminal element
> No AG is assumed. As established on [[Def - Hom-Functor and Representable Functor]], a solution functor $C : \mathbf{CRing} \to \mathbf{Set}$ — say $C(R) = \{(a,b) \in R^2 : b^2 = a^3 - 1\}$ — is an **affine scheme** exactly when it is representable. The category of elements $\int C$ has as objects pairs $(R, (a, b))$: a ring together with a chosen solution. A morphism $(R, (a,b)) \to (R', (a', b'))$ is a ring map $R \to R'$ carrying the solution $(a,b)$ to $(a',b')$. The functor $C$ is representable — i.e. an affine scheme — precisely when $\int C$ has an *initial* object (covariant case): a ring $A$ with a "generic solution" $(x, y) \in C(A)$ such that every concrete solution in every ring is obtained from it by a unique ring map. That initial object is $\big(A, (x, y)\big)$ with $A = \mathbb{Z}[x,y]/(y^2 - x^3 + 1)$. The categorical concept illustrated is "representability = existence of an initial/terminal element", and it is illuminating because it gives a *uniform* criterion: a functor of points is a scheme exactly when it has a generic point in this categorical sense.

**Is NOT an instance of having a terminal object — the covariant power-set functor.** The category of elements of the covariant power-set functor $\mathcal{P} : \mathbf{Set} \to \mathbf{Set}$ has *no* initial object, which is the structural reason $\mathcal{P}$ is not representable (see [[Def - Hom-Functor and Representable Functor]] and [[Ex - A non-representable functor]]). One can witness this directly: any candidate generic element $(A, S)$ fails the unique-factorization property because direct images cannot match arbitrary subsets uniquely.

**Calibration check.** Build $\int F$ for $F = \mathcal{C}(-, A)$ and verify its terminal object is $(A, 1_A)$. Confirm the projection $\pi : \int F \to \mathcal{C}$ sends this terminal object to $A$, recovering the representing object. For a covariant $F$, check that the morphism condition becomes $F(f)(x) = y$ and that universality means *initiality*, not terminality.

---

# Unlocked by This

> [!tip] Universal = Initial or Terminal *(from this chapter)*
> The category of elements proves [[Thm - Uniqueness of Universal Objects|the master theorem]]: a [[Def - Universal Element|universal element]] is an initial/terminal object of $\int F$, so representability is the existence of such an object, and the word "universal" is exactly a synonym for "initial or terminal".

> [!tip] The Grothendieck Construction and Fibrations *(from Higher Category Theory)*
> The category-of-elements construction is the $\mathbf{Set}$-valued case of the **Grothendieck construction**, which builds a fibration $\int F \to \mathcal{C}$ from a functor $F : \mathcal{C}^{op} \to \mathbf{Cat}$. This equivalence between fibrations and functors is foundational for **descent**, **stacks**, and the $\infty$-categorical theory of (co)cartesian fibrations.

> [!tip] Density and Free Cocompletion *(from this chapter)*
> Via $\int F \cong (\mathbf{y} \downarrow F)$, the category of elements encodes the *density theorem*: every presheaf $F$ is the colimit of the representables mapping into it, $F \cong \mathrm{colim}_{(A, x) \in \int F} \mathbf{y}A$. This is why $[\mathcal{C}^{op}, \mathbf{Set}]$ is the free cocompletion of $\mathcal{C}$.

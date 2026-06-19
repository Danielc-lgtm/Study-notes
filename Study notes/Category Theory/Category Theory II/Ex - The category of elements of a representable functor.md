---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Category of Elements"
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Universal Element"
  - "Def - Initial and Terminal Object"
tags: [category-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a locally small category and $A \in \mathcal{C}$.

1. Show that the [[Def - Category of Elements|category of elements]] of the representable presheaf $\mathcal{C}(-, A)$ is the **slice category** $\mathcal{C}/A$ (objects are morphisms $f : B \to A$; morphisms are commuting triangles over $A$).
2. Show that $(A, 1_A)$ is the **terminal object** of $\int \mathcal{C}(-, A) = \mathcal{C}/A$, and that it is the [[Def - Universal Element|universal element]].
3. Conclude that every representable functor has a universal element, and explain how this gives the "$\Leftarrow$" direction of "$F$ representable $\iff$ $\int F$ has a terminal object".

**Recall:**

![[Def - Category of Elements#The Definition]]

The [[Def - Category of Elements|category of elements]] $\int F$ of a presheaf $F : \mathcal{C}^{op} \to \mathbf{Set}$ has objects $(B, x)$ with $x \in F(B)$ and morphisms $(B, x) \to (B', x')$ the maps $f : B \to B'$ with $F(f)(x') = x$. A [[Def - Universal Element|universal element]] is a terminal object of $\int F$ (contravariant case).

---

# Convergent Strategy

**Problem class:** This is a "compute a category of elements and locate its terminal object" exercise — the concrete instantiation of the §2.4 machinery. The routine is to write out $\int F$ for the specific $F = \mathcal{C}(-, A)$, recognize the resulting category as a slice, and identify the obvious terminal object.

**Assumption pattern:** The decisive feature is that $F$ is *representable* — indeed it is literally a hom-functor, the most transparent case. The elements of $\mathcal{C}(-, A)$ are morphisms into $A$, so the category of elements is "objects-over-$A$", and the identity $1_A$ sits at the top as the universal point.

**Theorem routing:** The route is: (i) unwind the definition of $\int \mathcal{C}(-, A)$ — objects are pairs $(B, f : B \to A)$, morphisms are maps respecting restriction — and recognize this as the slice $\mathcal{C}/A$; (ii) check $(A, 1_A)$ is terminal by exhibiting, for each $(B, f)$, the unique morphism $(B, f) \to (A, 1_A)$ (it is $f$ itself); (iii) invoke the [[Def - Category of Elements|criterion]] that a terminal object of $\int F$ is the universal element.

**Key decision point:** The crux is seeing that the unique morphism $(B, f) \to (A, 1_A)$ in the slice is $f$ *itself*: it must be a map $g : B \to A$ with $\mathcal{C}(-, A)(g)(1_A) = f$, i.e. $1_A \circ g = f$, forcing $g = f$. Recognizing that the restriction condition pins $g = f$ uniquely is the heart of the terminality argument.

---

# Legal Operations Used

1. **Operation 7 from the topic page (test representability via the category of elements).** We build $\int \mathcal{C}(-, A)$ and locate its terminal object, the universal element.

2. **Operation 1 from the topic page (translate universality into a hom-set count).** Terminality of $(A, 1_A)$ is verified as "a singleton hom-set into it from every object", here forced by the restriction condition.

---

# Hints

> [!note]- Hint 1
> An object of $\int \mathcal{C}(-, A)$ is a pair $(B, f)$ with $f \in \mathcal{C}(B, A)$ — that is, a morphism into $A$. What category has morphisms-into-$A$ as its objects?

> [!note]- Hint 2
> A morphism $(B, f) \to (B', f')$ is a map $g : B \to B'$ with $\mathcal{C}(g, A)(f') = f$, i.e. $f' \circ g = f$ — a commuting triangle over $A$. So $\int \mathcal{C}(-, A) = \mathcal{C}/A$, the slice category.

> [!note]- Hint 3
> Terminal object: find $(T, t)$ such that every $(B, f)$ has a unique morphism to it. Try $(A, 1_A)$.

> [!note]- Hint 4
> A morphism $(B, f) \to (A, 1_A)$ is a $g : B \to A$ with $1_A \circ g = f$, forcing $g = f$ — unique. So $(A, 1_A)$ is terminal, hence the universal element.

---

# Solution

The plan is to unwind $\int \mathcal{C}(-, A)$ as the slice $\mathcal{C}/A$, then observe the identity $1_A$ sits at the top as the unique terminal object, which is by definition the universal element — establishing that representables always have one.

**Step 1: The category of elements is the slice category.**

> [!note]- Derivation
> Objects of $\int \mathcal{C}(-, A)$ are pairs $(B, f)$ with $f \in \mathcal{C}(-, A)(B) = \mathcal{C}(B, A)$ — exactly morphisms $f : B \to A$ into $A$. A morphism $(B, f) \to (B', f')$ is a map $g : B \to B'$ in $\mathcal{C}$ with $\mathcal{C}(g, A)(f') = f$; since $\mathcal{C}(g, A)$ is precomposition by $g$, this says $f' \circ g = f$, a commuting triangle with apex $A$. This is precisely the **slice category** $\mathcal{C}/A$: objects are arrows into $A$, morphisms are commuting triangles over $A$. So $\int \mathcal{C}(-, A) \cong \mathcal{C}/A$.

**Step 2: $(A, 1_A)$ is terminal and is the universal element.**

> [!note]- Derivation
> Consider the object $(A, 1_A) \in \mathcal{C}/A$ (the identity arrow $A \to A$). For any object $(B, f)$, a morphism $(B, f) \to (A, 1_A)$ is a map $g : B \to A$ with $1_A \circ g = f$, i.e. $g = f$. So there is exactly one such morphism, namely $f$ itself. Hence $(A, 1_A)$ is the [[Def - Initial and Terminal Object|terminal object]] of $\mathcal{C}/A = \int \mathcal{C}(-, A)$. By the [[Def - Category of Elements|criterion]], a terminal object of $\int F$ is a [[Def - Universal Element|universal element]] of $F$; so $(A, 1_A)$ is the universal element of $\mathcal{C}(-, A)$ — matching the general fact that the universal element of a representable functor is the image of the identity.

**Step 3: Representable $\Rightarrow$ universal element exists.**

> [!note]- Derivation
> If $F$ is representable, $F \cong \mathcal{C}(-, A)$ for some $A$, and this isomorphism induces an isomorphism of categories of elements $\int F \cong \int \mathcal{C}(-, A) = \mathcal{C}/A$ (a natural isomorphism of functors gives an isomorphism of their Grothendieck constructions). Since $\mathcal{C}/A$ has the terminal object $(A, 1_A)$, so does $\int F$, and that terminal object is the universal element. This is the easy "$\Rightarrow$" half of the [[Thm - Uniqueness of Universal Objects|representability criterion]]; the surprising converse — that a terminal object in $\int F$ *forces* representability — is the content of the Yoneda-based proof in [[Def - Category of Elements]].

> [!note]- Complete formal solution
> Objects of $\int \mathcal{C}(-, A)$ are morphisms $f : B \to A$; a morphism $(B, f) \to (B', f')$ is $g : B \to B'$ with $f' \circ g = f$. This is the slice category $\mathcal{C}/A$. The object $(A, 1_A)$ is terminal: a morphism $(B, f) \to (A, 1_A)$ is $g$ with $1_A \circ g = f$, forcing $g = f$, uniquely. So $(A, 1_A)$ is the universal element of $\mathcal{C}(-, A)$. For any representable $F \cong \mathcal{C}(-, A)$, $\int F \cong \mathcal{C}/A$ inherits this terminal object, proving representability implies the existence of a universal element. $\blacksquare$

---

# Key Takeaways

**The category of elements of a representable functor is just "objects over the representing object", with the identity as its peak.** This is the cleanest possible illustration of the §2.4 philosophy: when $F$ is the hom-functor $\mathcal{C}(-, A)$, its category of elements is the slice $\mathcal{C}/A$, and the universal element is the identity $1_A$ sitting at the terminal apex. The trigger to recognize a slice category is "objects are arrows into a fixed target $A$"; the reaction is "this is $\mathcal{C}/A = \int \mathcal{C}(-, A)$, with terminal object $1_A$". This concrete case is the model against which the abstract representability criterion should always be checked.

**The universal element is the image of the identity, made visible as a terminal object.** Across the whole chapter, the recurring slogan "the universal element is $\eta_A(1_A)$" gets its geometric meaning here: the identity $1_A$ is literally the terminal object of the category of elements. The unique morphism from any $(B, f)$ to $(A, 1_A)$ is $f$ itself, which is the categorical way of saying "every element factors uniquely through the universal one". Internalizing this picture — the universal element as the top of the slice — makes the representability criterion intuitive rather than formal.

**This is the "easy half" that motivates the hard half.** Proving "representable $\Rightarrow$ universal element exists" is immediate, as shown here. The genuinely surprising direction — that the mere existence of a terminal object in $\int F$ *forces* $F$ to be representable — is where the Yoneda lemma does real work (see [[Def - Category of Elements]] and [[Thm - Uniqueness of Universal Objects]]). Understanding the easy direction first is the right scaffolding: it shows what a universal element looks like in the transparent case, so that when you later build $\int F$ for a mystery functor and find a terminal object, you recognize it as exactly the structure that representability would have produced.

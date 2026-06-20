---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Generalized Multicategory"
  - "Def - Cartesian Monad"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $T = \mathrm{id}$ be the identity monad on $\mathbf{Set}$. Show that a $T$-[[Def - Generalized Multicategory|multicategory]] is exactly a small [[Def - Category|category]]: unwind the data $(C_0, C_1, \mathrm{dom}, \mathrm{cod}, \mathrm{ids}, \mathrm{comp})$ and the associativity/unitality axioms, verify that they coincide term-by-term with the data and axioms of a small category, and check that morphisms of $\mathrm{id}$-multicategories are exactly functors — so that $(\mathbf{Set}, \mathrm{id})\text{-}\mathbf{Multicat} \cong \mathbf{Cat}$.

**Recall:**

![[Def - Generalized Multicategory#The Definition]]

A small [[Def - Category|category]] $\mathcal{C}$ consists of a set $\mathrm{ob}\,\mathcal{C}$ of objects, a set $\mathrm{mor}\,\mathcal{C}$ of arrows, source and target maps $\mathrm{dom}, \mathrm{cod} : \mathrm{mor}\,\mathcal{C} \to \mathrm{ob}\,\mathcal{C}$, an identity map $\mathrm{id} : \mathrm{ob}\,\mathcal{C} \to \mathrm{mor}\,\mathcal{C}$, and a composition $\circ$ defined on composable pairs $\{(g, f) : \mathrm{dom}(g) = \mathrm{cod}(f)\}$, satisfying associativity $(h \circ g) \circ f = h \circ (g \circ f)$ and unitality $f \circ \mathrm{id} = f = \mathrm{id} \circ f$.

---

# Convergent Strategy

**Problem class:** This is an *unwinding* problem (the second target of the chapter): substitute the concrete monad into the generalized definition and recognize the classical axioms. The routine is to compute $T C_0$, rewrite each structure map, and match the axioms.

**Assumption pattern:** The decisive substitution is $T = \mathrm{id}$, which makes $T C_0 = C_0$ — so the domain map $\mathrm{dom} : C_1 \to T C_0$ becomes an *ordinary* source map $C_1 \to C_0$. Once that single simplification is in place, every other piece of the $T$-multicategory definition reverts to its category counterpart, because the identity monad introduces no arities.

**Theorem routing:** The route is direct from the [[Def - Generalized Multicategory|definition of a $T$-multicategory]] with $T = \mathrm{id}$; the conclusion is the $T = \mathrm{id}$ case of [[Thm - Generalized Operads Recover Classical Structures]]. To prove the equivalence rigorously, exhibit functors both ways and check they are mutually inverse on objects *and* morphisms.

**Key decision point:** The non-obvious obligation is to verify the claim at the level of *morphisms*, not just objects. It is easy to see the data of a $\mathrm{id}$-multicategory match the data of a category; the equivalence requires also that a morphism of $\mathrm{id}$-multicategories (a pair of maps commuting with the structure) is exactly a functor. Skipping this leaves only an object-level analogy. The natural shortcut of "the data match, so we are done" is precisely the trap.

---

# Legal Operations Used

1. **Operation 1 from the topic page (specialize the monad to read off a classical structure).** Setting $T = \mathrm{id}$ and computing $T C_0 = C_0$ is exactly this operation.
2. **Operation 4 from the topic page (form the composable-configuration pullback).** With $T = \mathrm{id}$ the pullback $C_1 \times_{C_0} C_1$ is the composable pairs.
3. **Operation 5 from the topic page (translate between span data and monad-graph data).** Matching the associativity axiom to the category axiom uses the monad-graph (explicit-maps) form.

---

# Hints

> [!note]- Hint 1
> Write out the six pieces of data of a $\mathrm{id}$-multicategory and set $T C_0 = C_0$ everywhere. Which classical category data does each piece become?

> [!note]- Hint 2
> The composition map is $\mathrm{comp} : C_1 \times_{T C_0} T C_1 \to C_1$. With $T = \mathrm{id}$ this is $C_1 \times_{C_0} C_1 \to C_1$. Describe the pullback $C_1 \times_{C_0} C_1$ as a set of pairs of arrows.

> [!note]- Hint 3
> For the equivalence, define $\Phi$ sending a $\mathrm{id}$-multicategory to "the same data, read as a category", and $\Psi$ the reverse. A morphism of $\mathrm{id}$-multicategories is $(f_0, f_1)$ with $f_1$ commuting with $\mathrm{dom}, \mathrm{cod}, \mathrm{ids}, \mathrm{comp}$ — check these four conditions are exactly "$f$ preserves sources, targets, identities, and composition", i.e. functoriality.

---

# Solution

The plan: substitute $T = \mathrm{id}$, identify the data and axioms with those of a category (Step 1), describe the composition pullback as composable pairs and match associativity/unitality (Step 2), then build the comparison functors and check they are mutually inverse on objects and morphisms (Step 3).

**Step 1: The data of a $\mathrm{id}$-multicategory are the data of a category.**

> [!note]- Derivation
> With $T = \mathrm{id}$, we have $T C_0 = C_0$ and $T C_1 = C_1$. The data of a $T$-multicategory become:
> - $C_0$ — a set; read as the *objects*.
> - $C_1$ — a set; read as the *arrows*.
> - $\mathrm{dom} : C_1 \to T C_0 = C_0$ — read as the *source* map.
> - $\mathrm{cod} : C_1 \to C_0$ — the *target* map (unchanged).
> - $\mathrm{ids} : C_0 \to C_1$ — read as the *identity-assigning* map.
> - $\mathrm{comp} : C_1 \times_{C_0} C_1 \to C_1$ — read as *composition*.
> These are precisely the data of a small category. The identity monad introduces no arities, so $\mathrm{dom}$ assigns each arrow a single source object, exactly as in a category.

**Step 2: The composition pullback is composable pairs, and the axioms match.**

> [!note]- Derivation
> The composition domain is the pullback of $\mathrm{dom} : C_1 \to T C_0 = C_0$ against $T(\mathrm{cod}) = \mathrm{cod} : C_1 \to C_0$, namely
> $$C_1 \times_{C_0} C_1 = \{(g, f) \in C_1 \times C_1 : \mathrm{dom}(g) = \mathrm{cod}(f)\},$$
> the set of composable pairs. So $\mathrm{comp}(g, f)$ is defined exactly when $\mathrm{dom}(g) = \mathrm{cod}(f)$ — the classical composability condition. The [[Def - Generalized Multicategory|$T$-multicategory]] associativity axiom states that the two ways of composing a composable triple agree, $\mathrm{comp}(\mathrm{comp}(h,g), f) = \mathrm{comp}(h, \mathrm{comp}(g,f))$, which is $(h \circ g) \circ f = h \circ (g \circ f)$. The unitality axiom states that grafting identities returns the arrow: $\mathrm{comp}(\mathrm{ids}(\mathrm{cod}(f)), f) = f = \mathrm{comp}(f, \mathrm{ids}(\mathrm{dom}(f)))$, i.e. $\mathrm{id} \circ f = f = f \circ \mathrm{id}$. Both are exactly the category axioms.

**Step 3: The equivalence of categories, on objects and morphisms.**

> [!note]- Derivation
> Define $\Phi : (\mathbf{Set}, \mathrm{id})\text{-}\mathbf{Multicat} \to \mathbf{Cat}$ by reading the data of Step 1 as a small category, and $\Psi : \mathbf{Cat} \to (\mathbf{Set}, \mathrm{id})\text{-}\mathbf{Multicat}$ by reading a small category's data as a $\mathrm{id}$-multicategory. On objects, $\Phi$ and $\Psi$ are mutually inverse by Steps 1–2 (the data and axioms are literally the same).
>
> On morphisms: a morphism of $\mathrm{id}$-multicategories $C \to C'$ is a pair $(f_0 : C_0 \to C_0', f_1 : C_1 \to C_1')$ with
> $$\mathrm{dom}' \circ f_1 = T f_0 \circ \mathrm{dom} = f_0 \circ \mathrm{dom}, \quad \mathrm{cod}' \circ f_1 = f_0 \circ \mathrm{cod}, \quad \mathrm{ids}' \circ f_0 = f_1 \circ \mathrm{ids}, \quad \mathrm{comp}' \circ (f_1 \times f_1) = f_1 \circ \mathrm{comp}.$$
> The first two say $f_1$ preserves source and target; the third says it preserves identities; the fourth says it preserves composition. These are exactly the axioms for $(f_0, f_1)$ to be a [[Def - Functor|functor]]. So $\Phi, \Psi$ are bijective on hom-sets and mutually inverse, giving $(\mathbf{Set}, \mathrm{id})\text{-}\mathbf{Multicat} \cong \mathbf{Cat}$ (an isomorphism, hence an equivalence).

> [!note]- Complete formal solution
> With $T = \mathrm{id}$, $T C_0 = C_0$ and $T C_1 = C_1$, so the data $(C_0, C_1, \mathrm{dom} : C_1 \to C_0, \mathrm{cod} : C_1 \to C_0, \mathrm{ids} : C_0 \to C_1, \mathrm{comp} : C_1 \times_{C_0} C_1 \to C_1)$ are exactly the data of a small category, with $\mathrm{comp}$ defined on composable pairs $\{(g,f) : \mathrm{dom}(g) = \mathrm{cod}(f)\}$. The associativity and unitality axioms of the $T$-multicategory are the associativity and unitality axioms of a category. A morphism of $\mathrm{id}$-multicategories $(f_0, f_1)$ satisfies the four commutativity conditions, which assert preservation of source, target, identities, and composition — i.e. functoriality. Hence the assignment of data is a functor $\Phi : (\mathbf{Set},\mathrm{id})\text{-}\mathbf{Multicat} \to \mathbf{Cat}$ with inverse $\Psi$, mutually inverse on objects and morphisms, so the two categories are isomorphic (in particular equivalent). $\blacksquare$

---

# Key Takeaways

**Computing $T C_0$ is the whole unwinding, and for the identity monad it changes nothing.** The single most important number in any generalized-multicategory problem is "what is $T C_0$?", because it determines what the domain of an arrow is allowed to be. With $T = \mathrm{id}$ the answer is "just $C_0$", so the domain is an ordinary source, the composition pullback is composable pairs, and the whole structure is a category. The reusable habit is to start every unwinding by writing $T C_0$ explicitly; once that object is understood, every structure map and every axiom follows mechanically. This is the template you reuse in [[Ex - A classical operad is a free-monoid-operad]], where $T C_0$ becomes lists and the same procedure produces a multicategory.

**An equivalence of categories is a claim about morphisms, not just objects, and the morphism check is where the real verification lives.** It is seductive to declare victory once the data of a $\mathrm{id}$-multicategory are seen to match the data of a category, but that only establishes a bijection on objects. The substance is that a *morphism* of $\mathrm{id}$-multicategories unwinds, condition by condition, into a functor — preservation of source, target, identities, and composition. The trigger to carry forward: whenever a problem asks to identify two categories of structures, budget half the work for the morphisms, because object-level coincidence is necessary but never sufficient, and the morphism conditions are exactly where a sloppy "equivalence" turns out to be only an analogy.

**The identity monad is the conservativity check: the framework must not change ordinary category theory.** A good generalization should specialize back to its starting point untouched, and this exercise is the proof that it does — $T = \mathrm{id}$ recovers exactly $\mathbf{Cat}$, no more and no less. This matters because it certifies that everything proved generically about $T$-multicategories (free constructions, algebras, limits) is, in the identity case, a genuine statement about ordinary categories, so the abstraction costs nothing at the base. The diagnostic to remember: if a purported generalization of categories did *not* recover $\mathbf{Cat}$ at $T = \mathrm{id}$, it would be modelling something else, and the identity-monad check is the fastest way to catch such a mismatch.

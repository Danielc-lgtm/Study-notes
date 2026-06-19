---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Cartesian Closed Category"
  - "Def - Adjunction"
  - "Def - Initial and Terminal Object"
tags: [category-theory, foundations]
---

# Problem Statement

The **Curry-Howard-Lambek correspondence** matches three trinities: cartesian closed categories, the simply typed lambda calculus, and intuitionistic propositional logic.

**(a)** Write out the dictionary: what categorical structure corresponds to a *type/proposition*, to a *term/proof*, to *conjunction/product type*, to *implication/function type*, to *truth*?

**(b)** Show that the currying isomorphism $\mathcal{C}(A\times B, C)\cong\mathcal{C}(A, C^B)$ is simultaneously the **deduction theorem** of logic and the typing rule for **$\lambda$-abstraction**.

**(c)** Explain in what precise sense "the simply typed lambda calculus is the internal language of cartesian closed categories", and identify the Heyting-algebra (poset) special case as intuitionistic propositional logic.

**Recall:**

![[Def - Cartesian Closed Category#The Definition]]

A [[Def - Cartesian Closed Category|cartesian closed category]] has finite products and exponentials with $\mathcal{C}(A\times B, C)\cong\mathcal{C}(A, C^B)$. The [[Def - Initial and Terminal Object|terminal object]] $1$ is the empty product. A **Heyting algebra** is a cartesian closed poset.

---

# Convergent Strategy

**Problem class:** This is a "build a correspondence / interpret one structure as another" problem (⭐⭐⭐) — the flagship Cluster-10 bridge linking category theory, logic, and computation. The work is conceptual: matching three vocabularies and showing the categorical bijection is the logical/computational rule.

**Assumption pattern:** The structural facts are: the CCC bijection $\mathcal{C}(A\times B, C)\cong\mathcal{C}(A, C^B)$, the terminal object as "true", products as conjunction, exponentials as implication. The correspondence is forced once these matches are fixed — currying becomes the deduction theorem, evaluation becomes modus ponens.

**Theorem routing:** Fix the dictionary (a) $\Rightarrow$ read currying as deduction theorem / $\lambda$-abstraction (b) $\Rightarrow$ state the internal-language theorem (free CCC $=$ simply typed lambda calculus) and specialise to posets/Heyting algebras for intuitionistic logic (c).

**Key decision point:** The crucial recognition is that *a morphism is both a proof and a program*: $A\to B$ is a proof of $A\vdash B$ and a program of type $A\to B$, and composition is both cut (logic) and substitution (computation). This triple identification is what makes the correspondence an equivalence of theories, not a loose analogy. The non-obvious payoff is that the *free* CCC is exactly the syntax of the lambda calculus.

---

# Legal Operations Used

1. **Operation 10 from the topic page (curry in a cartesian closed category).** Currying is the deduction theorem / $\lambda$-abstraction.

2. **Operation 1 from the topic page (transpose across the adjunction).** Evaluation (counit) is modus ponens / application.

3. **Operation 7 from the topic page (Galois connection as adjunction between posets).** The Heyting-algebra case is the poset specialisation, where the CCC is a cartesian closed poset.

---

# Hints

> [!note]- Hint 1
> Objects = types = propositions; morphisms $A\to B$ = programs of type $A\to B$ = proofs of $A\vdash B$; product = conjunction = pair type; exponential = implication = function type; terminal $1$ = $\top$ = unit type.

> [!note]- Hint 2
> The deduction theorem says "$A\wedge B\vdash C$ iff $A\vdash B\Rightarrow C$". Read $\vdash$ as "there is a morphism": $\mathcal{C}(A\times B, C)\neq\emptyset$ iff $\mathcal{C}(A, C^B)\neq\emptyset$. The currying bijection says more — the *proofs/programs* correspond, not just provability.

> [!note]- Hint 3
> "Internal language": the free CCC on a set of base types has, as its morphisms, exactly the (βη-equivalence classes of) simply typed lambda terms. Building the CCC *is* the type theory. In the poset case, a CCC is a Heyting algebra and the morphisms-or-not encode intuitionistic provability (no double-negation elimination, since $\neg\neg a = a$ fails).

---

# Solution

The correspondence is a dictionary plus one theorem. The dictionary matches the three vocabularies; the theorem says the free CCC is the lambda calculus. Currying is the deduction theorem; evaluation is modus ponens.

**Step 1: The dictionary (part a).**

> [!note]- Derivation
> | Category theory (CCC) | Type theory ($\lambda$-calculus) | Logic (intuitionistic) |
> |---|---|---|
> | object $A$ | type $A$ | proposition $A$ |
> | morphism $f : A\to B$ | term/program $x:A\vdash f(x):B$ | proof of $A\vdash B$ |
> | identity $1_A$ | variable $x:A\vdash x:A$ | axiom $A\vdash A$ |
> | composition $g\circ f$ | substitution | cut |
> | terminal object $1$ | unit type | $\top$ (true) |
> | product $A\times B$ | pair type $A\times B$ | conjunction $A\wedge B$ |
> | projections $\pi_1, \pi_2$ | $\mathtt{fst}, \mathtt{snd}$ | $\wedge$-elimination |
> | pairing $\langle f, g\rangle$ | $(f, g)$ | $\wedge$-introduction |
> | exponential $C^B$ | function type $B\to C$ | implication $B\Rightarrow C$ |
> | evaluation $\mathrm{ev}$ | application | modus ponens |
> | currying $\widehat{(-)}$ | $\lambda$-abstraction | deduction theorem |
> | initial object $0$ | empty type | $\bot$ (false) |
> | coproduct $A + B$ | sum type | disjunction $A\vee B$ |
>
> The central insight: **a morphism is simultaneously a program and a proof.** Composition is substitution (computation) and cut (logic). This is why the three theories are equivalent, not merely analogous.

**Step 2: Currying $=$ deduction theorem $=$ $\lambda$-abstraction (part b).**

> [!note]- Derivation
> The currying isomorphism is $\mathcal{C}(A\times B, C)\cong\mathcal{C}(A, C^B)$, i.e. $\mathcal{C}(A\wedge B, C)\cong\mathcal{C}(A, B\Rightarrow C)$.
>
> **As logic (deduction theorem).** A proof of $C$ from the hypotheses $A$ and $B$ (i.e. from $A\wedge B$) is the same as a proof of $B\Rightarrow C$ from the single hypothesis $A$. "Discharge the hypothesis $B$ into an implication." The bijection says these proofs correspond perfectly — this is exactly the deduction theorem $A\wedge B\vdash C\iff A\vdash B\Rightarrow C$.
>
> **As type theory ($\lambda$-abstraction).** A program $f$ taking inputs of type $A$ and $B$ and returning $C$ is the same as a program taking an $A$ and returning a *function* $B\to C$. The forward direction is $\lambda$-abstraction: $\widehat{f} = \lambda b. f(a, b)$, abstracting the second argument. The inverse is application. The first triangle identity $\mathrm{ev}\circ(\widehat{f}\times 1) = f$ is the $\beta$-reduction rule $(\lambda b. f(a,b))(b') = f(a, b')$; the uniqueness clause is $\eta$-expansion.
>
> So the single categorical bijection is the deduction theorem and the abstraction/application rules at once: currying $\leftrightarrow$ "discharge a hypothesis" $\leftrightarrow$ "abstract an argument".

**Step 3: Internal language and the Heyting-algebra case (part c).**

> [!note]- Derivation
> **Internal language theorem.** The simply typed lambda calculus (with product and function types) over a signature of base types and basic terms generates a CCC: take types as objects, βη-equivalence classes of terms-in-one-free-variable as morphisms. This CCC is the *free* cartesian closed category on the signature. Conversely every CCC interprets the lambda calculus (the dictionary of Step 1 sends each typing rule to a categorical operation, soundly). The two passages are inverse up to equivalence: **the lambda calculus is the internal language of CCCs, and CCCs are the categorical semantics of the lambda calculus.** "Internal language" means: reasoning about objects and morphisms of any CCC can be carried out *as if* writing typed programs, and the syntax is complete for this reasoning.
>
> **Heyting-algebra (poset) case.** When the CCC is a [[Def - Initial and Terminal Object|poset]] — at most one morphism per hom-set — it is a **Heyting algebra**: finite meets ($\wedge$), finite joins ($\vee$), and a Heyting implication $a\Rightarrow b$ with $c\leq(a\Rightarrow b)\iff c\wedge a\leq b$ (currying). Here a morphism either exists or not, so the structure records *provability* rather than *proofs*: $a\leq b$ means "$a$ entails $b$" in **intuitionistic propositional logic**. Crucially, $\neg\neg a = a$ fails in a general Heyting algebra (e.g. the opens of a space: $\neg\neg U = \mathrm{int}(\overline{U})\neq U$), which is exactly the failure of the law of excluded middle / double-negation elimination — Heyting algebras model intuitionistic, not classical, logic. The classical case ($\neg\neg a = a$ for all $a$) recovers Boolean algebras.

> [!note]- Complete formal solution
> **(a)** Dictionary: object/type/proposition; morphism/program/proof; product/pair-type/conjunction; exponential/function-type/implication; terminal/unit-type/$\top$; coproduct/sum-type/disjunction; initial/empty-type/$\bot$. Composition is substitution and cut. A morphism is at once a program and a proof.
>
> **(b)** Currying $\mathcal{C}(A\times B, C)\cong\mathcal{C}(A, C^B)$ is the deduction theorem ($A\wedge B\vdash C\iff A\vdash B\Rightarrow C$) and the typing rule for $\lambda$-abstraction; the counit (evaluation) is modus ponens / application; the triangle identity is $\beta$-reduction.
>
> **(c)** The free CCC on a signature is the simply typed lambda calculus over that signature (types = objects, βη-classes of terms = morphisms), and every CCC soundly interprets the calculus — so the calculus is the internal language of CCCs. In the poset case a CCC is a Heyting algebra, modelling intuitionistic propositional logic, with $\neg\neg a\neq a$ in general (no excluded middle); Boolean algebras are the classical sub-case. $\blacksquare$

---

# Key Takeaways

**A morphism is a proof and a program at once — this triple identification is the whole correspondence.** The deepest content of Curry-Howard-Lambek is that the *same mathematical object*, a morphism $A\to B$ in a cartesian closed category, is a proof of the entailment $A\vdash B$ and a program of type $A\to B$, with composition being simultaneously cut-elimination and substitution. This is not an analogy but an equivalence of three theories, and it is why proof assistants (Coq, Agda, Lean) work: checking a proof *is* type-checking a program, and constructing a proof *is* writing a program. The trigger to invoke this is any setting with "types and terms" or "propositions and proofs" carrying products and function spaces — it is automatically a CCC, and the categorical machinery (adjunctions, limits) becomes available to reason about it.

**Currying is the deduction theorem and $\lambda$-abstraction — one categorical bijection, three readings.** The currying isomorphism $\mathcal{C}(A\times B, C)\cong\mathcal{C}(A, C^B)$ is the load-bearing structure: logically it is "discharge a hypothesis into an implication" (the deduction theorem), computationally it is "abstract an argument into a function" ($\lambda$-abstraction), and categorically it is the adjunction $(-\times B)\dashv(-)^B$. Evaluation, its counit, is modus ponens and function application; the triangle identity is $\beta$-reduction. Recognising that these are *the same equation* is the moment the correspondence becomes operational — you can prove a logical fact by exhibiting a program, or vice versa, and translate freely. The companion exercise [[Ex - The exponential and currying in a cartesian closed category|The exponential and currying]] verifies the categorical side of this bijection concretely.

**The free CCC is the syntax, and the poset case is intuitionistic logic — this is the bridge to type theory and homotopy type theory.** "The simply typed lambda calculus is the internal language of cartesian closed categories" means the free CCC on a signature *is* the type theory: building the category and writing the programs are the same activity. Specialising to posets gives Heyting algebras, the algebraic semantics of intuitionistic propositional logic, where the failure of $\neg\neg a = a$ encodes the rejection of excluded middle. This is the entry point to the larger program: adding *dependent* types pushes CCCs to **locally cartesian closed categories**, and adding *identity types* with their higher structure pushes to **homotopy type theory**, where types are spaces, proofs of equality are paths, and the categorical home is a locally cartesian closed $\infty$-category. This ⭐⭐⭐ exercise is therefore the seed of the entire Cluster-10 logic/type-theory/category-theory program — the place where adjunctions become the grammar of computation and proof.
